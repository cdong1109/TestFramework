import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class SpecialAgreement(unittest.TestCase):
    """特别约定"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://14.17.100.220:8027/glsx-insurance/insurance/findAllPromise"

    def test_special_agreement_1(self):
        """1"""
        payload = {'channelCode': '0001', 'productCode': '000001'}
        
        r = requests.get(self.base_url,params=payload)
        result = r.json()
        self.assertEqual(r.status_code, 200)
        

        check_point = {"ok":True,"errorCode": "0"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
