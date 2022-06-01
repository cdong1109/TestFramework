from Util.DBOper import DB
from Config.VarConfig import *


def createScrpt():
    db = DB()
    apiList = db.getApiList()
    for api in apiList:
        apiCastList = db.getApiCaseList(api[0])
        for apiCase in apiCastList:
            createFile(api, apiCastList)


def createFile(api, apiCaseList):
    with open(scriptsDir + "\\" + "Script" + str(api[0]) +"_"+ api[3].title().replace("_", "") + ".py", "w",
              encoding="utf-8") as fp:
        fp.write(codeHead)
        if api[7] == 1 and api[8] == 1:
            fp.write(classHeadDB % (api[3].title().replace("_", ""), api[1], api[4]))
            for idx, case in enumerate(apiCaseList, 1):
                param_code = ""
                if case[3]:
                    param_code = '''payload = self.dbd.processRequestDependData(%s, %s)''' % (
                    eval(case[2]), eval(case[3]))
                else:
                    param_code = '''payload = %s''' % eval(case[2])
                encrypt_request_data = ""
                if case[4]:
                    encrypt_request_data = '''self.dbd.processEncryptData(%s,%s)''' % ("payload", eval(case[4]))
                store_code = ""
                if case[7]:
                    store_code = '''self.dbd.storeData(%s, %s, %s, %s, %s)''' % (
                    int(case[0]), int(case[1]), case[7], case[2] if case[2] else None, "result")
                if api[5].lower() == "post":
                    if api[6].lower() == "data":
                        fp.write(postDataCode % (
                        (api[3] + "_" + str(idx)), str(idx), param_code, encrypt_request_data, store_code))
                    elif api[6].lower() == "json":
                        fp.write(postJsonCode % (
                        (api[3] + "_" + str(idx)), str(idx), param_code, encrypt_request_data, store_code))
                elif api[5].lower() == "get":
                    if api[6].lower() == "params":
                        fp.write(getParamsCode % (
                        (api[3] + "_" + str(idx)), str(idx), param_code, encrypt_request_data, store_code))
                    elif api[6].lower() == "url":
                        fp.write(getUrlCode % (
                        (api[3] + "_" + str(idx)), str(idx), param_code, encrypt_request_data, store_code))
                if case[8]:
                    check_code = checkCode % case[8]
                    fp.write(check_code)
                fp.write(classEndDB)
                fp.write("\n" + codeEnd)