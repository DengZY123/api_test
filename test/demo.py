# import requests
#
# headers = {
#     'Cookie':"_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; boss_storagelist_show_type=1; boss_data_show_type=1; boss_fontsize_show_type=2; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561337982,1561424888,1561597329,1561684209; passport=2|1:0|10:1561687083|8:passport|24:NDUzMDIwNHwxNTYxNjg3MDgz|c38a5ed352ae18b678b9385689aef2a604a7f687ea780865d8b98bb57cd6a99d; passport_hash="+"2|1:0|10:1561687083|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|9b59b7e518fc3dfa474aee518538bdba74cdbe2ee244b2b4c9454b1b48ce40a2"+"; pfshop_id=2|1:0|10:1561687096|9:pfshop_id|4:MTA1|f98aa9a4b2d0240d2cea075497585258a42e0f3fe3a082aeff3c926669e20d38; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561687097",
#     'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# }
# data = {
#     "action": "get_goods",
#     "_xsrf" : "2|a617f5e1|412150a5ca384b8af5dacd0abe020a56|1560909123"
# }
# url = 'https://pf.senguo.cc/boss/goods/stockin'
# resp = requests.post(url, data=data,headers=headers).text
# print(resp)
import operator
import json
dict1 = {"text": "\u552e\u4ef7\u4f4e\u4e8e\u6210\u672c\u4ef7", "low_price": true, "success": true}
dict2 = {"Age":8,"Name":"deng"}
print(operator.eq(dict1,dict2))

