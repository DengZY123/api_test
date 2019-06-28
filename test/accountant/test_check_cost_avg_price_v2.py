# import sys
# sys.path.append("../..")  # 提升2级到项目根目录下
# from config.config import *  # 从项目路径下导入
# from lib.read_excel import *  # 从项目路径下导入
# import json
#
# data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")  # 读取TestUserReg工作簿的所有数据
# case_data = get_test_data(data_list, 'test_accountant_price')  # 从数据列表中查找到该用例数据
# if not case_data:  # 有可能为None
#     logging.error("用例数据不存在")
#
# url = case_data.get('url')  # excel中的标题也必须是小写url
#
# data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
# expect_res = case_data.get('expect_res')  # 期望数据
# r = json.loads(expect_res)
# print(r, type(r))
