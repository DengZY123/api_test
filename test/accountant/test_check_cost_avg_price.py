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

    def test_check_cost_price(self):

        case_data = get_test_data(self.data_list, 'test_accountant_price')  # 从数据列表中查找到该用例数据
        log_info("case_data", type(case_data))
        self.send_request(case_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
