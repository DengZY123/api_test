import operator
import unittest
import requests
import json
import sys

from config.config import data_path

sys.path.append("../..")  # 提升2级到项目根目录下

from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info, os, log_info  # 从项目路径下导入


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
         cls.data_list = excel_to_list((os.path.join(data_path, "test_user_data.xlsx")), "TestUserReg")

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        log_info("test_check_cost_price", "456")
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        log_info("test_check_cost_price", "123")
        headers = {
            'Cookie': "_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; boss_storagelist_show_type=1; boss_data_show_type=1; boss_fontsize_show_type=2; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561337982,1561424888,1561597329,1561684209; passport=2|1:0|10:1561687083|8:passport|24:NDUzMDIwNHwxNTYxNjg3MDgz|c38a5ed352ae18b678b9385689aef2a604a7f687ea780865d8b98bb57cd6a99d; passport_hash=" + "2|1:0|10:1561687083|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|9b59b7e518fc3dfa474aee518538bdba74cdbe2ee244b2b4c9454b1b48ce40a2" + "; pfshop_id=2|1:0|10:1561687096|9:pfshop_id|4:MTA1|f98aa9a4b2d0240d2cea075497585258a42e0f3fe3a082aeff3c926669e20d38; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561687097",
            'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        """
        if method.upper() == "GET":
            res = requests.get(url=url, data=data, headers=headers)
        elif method.upper() == "POST":
            res = requests.post(url=url, data=data, headers=headers)

        expect_res = json.loads(expect_res)
        reponse_text = json.loads(res.text)
        if operator.eq(reponse_text,expect_res):
            result = "测试通过"
        else :
            result = "测试失败"
            """
        result = "测试失败"
        data = json.loads(data)
        res = requests.post(url=url, data=data, headers=headers)
        expect_res = json.loads(expect_res)
        reponse_text = json.loads(res.text)

        log_case_info('test_accountant_cost_avg_price', url, data, expect_res, reponse_text,result)
       # self.assertEqual(reponse_text, expect_res)  # 断言






if __name__ == "__main__":
    unittest.main()
    print(issubclass(BaseCase,BaseCase))