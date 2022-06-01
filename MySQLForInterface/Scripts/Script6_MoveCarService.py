import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class MoveCarService(unittest.TestCase):
    """挪车服务"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://qcwx.glsx.com.cn/web-ddh-movecar/sendWechatMessage/"

    def test_move_car_service_1(self):
        """1"""
        payload = 102886
        
        r = requests.get(self.base_url + str(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        

        check_point = {"returnCode": "0", "message": "ok"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
