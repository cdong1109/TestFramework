import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class UserLogin(unittest.TestCase):
    """用户登录"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://39.106.41.11:8080/login/"

    def test_user_login_1(self):
        """1"""
        payload = self.dbd.processRequestDependData({'username': '', 'password': ''}, {'1->1': ['username', 'password']})
        self.dbd.processEncryptData(payload,{'password': ['md5']})
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        self.dbd.storeData(2, 2, {"response":["userid", "token"]}, {"username":"","password":""}, result)

        check_point = {"code": "00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
