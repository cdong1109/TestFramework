import unittest, requests
from Action.PublicInfo import *
import os, sys,json

class UserCreateBlog(unittest.TestCase):
    """新建博文"""
    def setUp(self):
        self.dbd = DBData()
        self.base_url = "http://39.106.41.11:8080/create/"

    def test_user_create_blog_1(self):
        """1"""
        payload = self.dbd.processRequestDependData({'userid': '', 'token': '', 'title': 'blog_title', 'content': 'blog_content'}, {'2->2': ['userid', 'token']})
        
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        

        check_point = {"code":"00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))

    def tearDown(self):
        self.dbd.closeConnect()


if __name__ == '__main__':
    unittest.main()
