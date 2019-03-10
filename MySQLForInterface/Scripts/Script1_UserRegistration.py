import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class UserRegistration(unittest.TestCase):
    """用户注册"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://39.106.41.11:8080/register/"

    def test_user_registration_1(self):
        """1"""
        payload = {'username': 'bbbbbdong26', 'password': 'dong123456', 'email': 'dong123456@qq.com'}
        
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        self.dbd.storeData(1, 1, {"request":["username","password"]}, {"username":"bbbbbdong26","password":"dong123456","email":"dong123456@qq.com"}, result)

        check_point = {"code":"00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
