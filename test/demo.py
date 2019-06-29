import requests

headers = {
    'Cookie':"_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; boss_data_show_type=1; boss_storagelist_show_type=1; boss_fontsize_show_type=2; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561424888,1561597329,1561684209,1561789248; passport_hash="+"2|1:0|10:1561797546|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|0a7b5201fa650cac1225f4b0fd6d244e326ca4d9fd5d14bc900bb92790926b76"+"; passport=2|1:0|10:1561797546|8:passport|24:NDUzMDIwNHwxNTYxNzk3NTQ2|9cae89e4544551eec6d7b461331b4da38c1b9bb124d75bba18725f003c3b446a; pfshop_id=2|1:0|10:1561797554|9:pfshop_id|4:NzI4|f851ce2d93eb88422700ae46d805703f11b51e4e6745ffd64c9f48ed3eb82fe6; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561797555",
    'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
data = {
    "action": "get_goods",
    "_xsrf" : "2|a617f5e1|412150a5ca384b8af5dacd0abe020a56|1560909123"
}
url = 'https://pf.senguo.cc/boss/goods/stockin'
resp = requests.post(url, data=data,headers=headers).text
print(resp)


