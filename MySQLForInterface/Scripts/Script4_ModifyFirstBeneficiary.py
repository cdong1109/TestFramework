import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class ModifyFirstBeneficiary(unittest.TestCase):
    """修改第一受益人"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://14.17.100.220:8027/glsx-insurance/insurance/updateInsurance"

    def test_modify_first_beneficiary_1(self):
        """1"""
        payload = {'channelCode': '0001', 'productCode': '000001', 'fullInsuranceNo': 'H10101040220181622518', 'compensationName': 'lisa'}
        
        r = requests.post(self.base_url, json = payload)
        result = r.json()
        self.assertEqual(r.status_code, 200)
        

        check_point = {"ok":True, "errorCode": "0"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
