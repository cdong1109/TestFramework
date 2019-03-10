import os

# 工程的根目录
baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试脚本存放目录
scriptsDir = baseDir + "/Scripts"

# 数据库配置文件的绝对路径
configPath = baseDir + "/Config/DBConfig.ini"

codeHead = '''import unittest, requests
from Action.PublicInfo import *
import os, sys,json
'''

# 无数据库链接时
classHead = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.base_url = "%s"
'''

# 有数据库链接时
classHeadDB = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "%s"
'''

classEndDB = '''
    def tearDown(self):
        self.dbd.closeConnect()
'''

codeEnd = '''
if __name__ == '__main__':
    unittest.main()
'''

postDataCode = '''
    def test_%s(self):
        """%s"""
        %s
        %s
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
postJsonCode = '''
    def test_%s(self):
        """%s"""
        %s
        %s
        r = requests.post(self.base_url, json = payload)
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
getParamsCode = '''
    def test_%s(self):
        """%s"""
        %s
        %s
        r = requests.get(self.base_url,params=payload)
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
getUrlCode = '''
    def test_%s(self):
        """%s"""
        %s
        %s
        r = requests.get(self.base_url + str(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
checkCode = '''
        check_point = %s
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))
'''
