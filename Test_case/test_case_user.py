import unittest
import json
from ddt import ddt, file_data, unpack
from Api_autotest_v3.Common.common_func import *
from Api_autotest_v3.Common.method import SendMain


@ddt
class TestSign(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @file_data('../Test_data/sign_data.json')
    @unpack
    def test_SignSuccess(self, value):
        url = link() + "/login"
        request_method = 'Post'
        payload = value[0]
        # header is in the common_func.py
        # four elements attribute for api

        r = SendMain(url, request_method, header, payload).req
        print(json.dumps(r, ensure_ascii=False, sort_keys=True, indent=2))  # print the response body
        print("-"*25 + "End" + "-"*25)

        self.assertEqual(200, r.get('status'), "Code should be 200!")  # Assert


if __name__ == '__main__':
    unittest.main()
