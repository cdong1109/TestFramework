import pymysql
from Util.EncryptMD5 import encryptMD5
from Util.ConfigDB import dbConfigParse
from Util.DBOper import DB
from datetime import datetime


class DBData(object):
    def __init__(self):
        self.db_conf = dbConfigParse()
        self.conn = pymysql.connect(
            host=self.db_conf["host"],
            port=self.db_conf["port"],
            user=self.db_conf["user"],
            passwd=self.db_conf["password"],
            db=self.db_conf["db"],
            charset="utf8"
        )
        # 设置数据库变更自动提交
        self.conn.autocommit(1)
        self.cur = self.conn.cursor()

    def getDependData(self, apiId, caseId):
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" % (apiId, caseId)
        self.cur.execute(sqlStr)
        # 字典对象
        rely_data = eval((self.cur.fetchall())[0][0])
        return rely_data

    def processRequestDependData(self, requestData, dependData):
        # 处理接口请求数据中依赖数据
        for key, value in dependData.items():
            apiId, caseId = key.split("->")
            relyDate = self.getDependData(apiId, caseId)
            for k, v in relyDate.items():
                if k in requestData:
                    requestData[k] = v
        return requestData

    def processEncryptData(self, sourceData, encryptReg):
        # 处理接口请求中的加密数据
        for key, value in encryptReg.items():
            if key in sourceData:
                for i in value:
                    if i.lower() == "md5":
                        # md5加密
                        sourceData[key] = encryptMD5(sourceData[key])
        return sourceData

    def storeData(self, apiId, caseId, storeDataReg, requestData=None, responseData=None):
        # 存储请求或相应数据中的数据,供后面的接口使用
        storeData = {}
        if "request" in storeDataReg:
            # 如果是“request”存储请求数据
            for i in storeDataReg["request"]:
                if i in requestData:
                    storeData[i] = requestData[i]
        if "response" in storeDataReg:
            # 如果是“response”存储响应数据
            for j in storeDataReg["response"]:
                if j in responseData:
                    storeData[j] = responseData[j]
        self.writeStoreData(apiId, caseId, storeData)

    def writeStoreData(self, apiId, caseId, storeData):
        # 在数据库表中存储依赖数据
        if self.hasDependData(apiId, caseId):
            sqlStr = 'update interface_data_store set data_store=\"%s\", ctime=\"%s\" where api_id=%s and case_id=%s'
            self.cur.execute(sqlStr % (storeData, datetime.now(), apiId, caseId))
        else:
            # 数据库中不存在这条数据，需要添加
            sqlStr = 'insert into interface_data_store values(%s, %s, \"%s\", \"%s\")'
            self.cur.execute(sqlStr % (apiId, caseId, storeData, datetime.now()))

    def hasDependData(self, apiId, caseId):
        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" % (apiId, caseId)
        # 获取受影响的条数，0表示没有查到数据，>0表示至少有一条数据
        affect_num = self.cur.execute(sqlStr)
        # 返回受影响的条数
        return affect_num

    def closeConnect(self):
        # 关闭数据连接
        self.conn.commit()
        self.cur.close()
        self.conn.close()