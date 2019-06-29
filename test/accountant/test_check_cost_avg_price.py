import unittest
import requests
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info ,log_info # 从项目路径下导入
import json
import operator
from test.case.BaseCase import BaseCase

class TestCheckPrice(BaseCase):
    """
    def test_check_cost_price(self):
        case_data = get_test_data(self.data_list, 'test_accountant_price')  # 从数据列表中查找到该用例数据
        self.send_request(case_data)
"""
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")  # 读取TestUserReg工作簿的所有数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_check_cost_price(self):
        log_info("ddd", "123")
        """
        log_info("ddd","123")
        case_data = get_test_data(self.data_list, 'test_accountant_price')  # 从数据列表中查找到该用例数据
        self.send_request(case_data)
        """
        case_data = get_test_data(self.data_list, 'test_accountant_price')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')   # excel中的标题也必须是小写url

        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据


        headers = {
            'Cookie': "_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; boss_storagelist_show_type=1; boss_data_show_type=1; boss_fontsize_show_type=2; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561337982,1561424888,1561597329,1561684209; passport=2|1:0|10:1561687083|8:passport|24:NDUzMDIwNHwxNTYxNjg3MDgz|c38a5ed352ae18b678b9385689aef2a604a7f687ea780865d8b98bb57cd6a99d; passport_hash=" + "2|1:0|10:1561687083|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|9b59b7e518fc3dfa474aee518538bdba74cdbe2ee244b2b4c9454b1b48ce40a2" + "; pfshop_id=2|1:0|10:1561687096|9:pfshop_id|4:MTA1|f98aa9a4b2d0240d2cea075497585258a42e0f3fe3a082aeff3c926669e20d38; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561687097",
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }

        res = requests.post(url=url, data=json.loads(data),headers=headers)  # 表单请求，数据转为字典格式
        expect_res = json.loads(expect_res)
        reponse_text = json.loads(res.text)
        if operator.eq(reponse_text,expect_res):
            result = "测试通过"
        else :
            result = "测试失败"
        log_case_info('test_accountant_cost_avg_price', url, data, expect_res, res.text,result)
        self.assertEqual(reponse_text, expect_res)  # 断言





if __name__ == '__main__':
    unittest.main(verbosity=2)
