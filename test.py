import csv
import urllib.parse
from datetime import datetime

import requests
import hashlib
import time
import json
import re

#手动输入em.token与cookie
# em_token = "17fc6bdc9c54402696099a85a00aeb43"
em_token = input("em.token:")

# cookie = \
#     'cookie2=1c73cfac4db0c028b4804eeb253c42af; _tb_token_=31e343e405bb7; cna=9Gi/HqkZLQ4CAXFftyTryaKX; thw=cn; _samesite_flag_=true; cancelledSubSites=empty; tracknick=tb9828473581; t=2ddbe724a3b4d543c34020775b5148eb; miid=859557833610723248; lgc=tb9828473581; dnk=tb9828473581; wk_cookie2=18e1f45a474c0e3476e892141605f677; wk_unb=UUphwoXxKCNsnUkZCw%3D%3D; 3PcFlag=1741765283278; unb=2208263923571; cookie17=UUphwoXxKCNsnUkZCw%3D%3D; _l_g_=Ug%3D%3D; sg=116; _nk_=tb9828473581; cookie1=BqU%2FbJvAZZemLywtHwAiafCTKwJx0FfyVxW%2F8PJisZo%3D; sgcookie=E1001nK6efyHo3afIq2uAXJE5pPaNzhwXmmPCIz2FUSwi61JJTdH82Plv7Ulp6W7eDzD99eZHFEiRETzHmb%2FqGFHTnBybuwlCf5jdnC49LGEGFQ%3D; havana_lgc2_0=eyJoaWQiOjIyMDgyNjM5MjM1NzEsInNnIjoiYjU1MWU1OTFjYzJiYmRjOTI5ZjFiYTljNjU5NzIwYjciLCJzaXRlIjowLCJ0b2tlbiI6IjFGdUJDSFJ6NVd6V2lRT0E3WG1QRy13In0; _hvn_lgc_=0; havana_lgc_exp=1772869685124; cookie3_bak=1c73cfac4db0c028b4804eeb253c42af; cookie3_bak_exp=1742024885124; uc1=cookie15=UtASsssmOIJ0bQ%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie14=UoYaiuTRp9wRvQ%3D%3D&pas=0&cookie21=Vq8l%2BKCLjA%2Bl&existShop=false; uc3=nk2=F5RMEYDYuuGXY9%2B0&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUphwoXxKCNsnUkZCw%3D%3D&vt3=F8dD2EjLGEuchUV2nJw%3D; csg=98b0bb1b; env_bak=FM%2BgmZzCKK9DuYqMpN0zlAHqQEJYZvgFSduKxFEcEwrh; skt=f94b6d796605ab78; existShop=MTc0MTc2NTY4NQ%3D%3D; uc4=nk4=0%40FY4HVFvXl98cO3Z1j7Ym1FVL14phOOE%3D&id4=0%40U2grGR1ikxRow5cg3lRfZesJqq1MDScE; _cc_=VT5L2FSpdA%3D%3D; sdkSilent=1741911037558; havana_sdkSilent=1741911037558; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=17fc6bdc9c54402696099a85a00aeb43_1741954139273; _m_h5_tk_enc=c6e5800a4b6ce685f1ac0edbfdf47e4d; tfstk=gpIoI5jfka8WjQrgVjt7WyRXKLUvd3tpYufp9BBeTLAXa0Be9Hfht6AJ87tRxsXFs89LNMH5l1BZ2gUWvDxWAHPT6lEOnTtBYVkD3y0S0p9zvYJzknP-3HqY6lEOFzJWvtPO2IszVIvtYH8y8Ko2GpcraD5eumJBg0JE4pl4nI9eY0JyLmo2BdGr405F3-vpgX-ez68qHL4yNMSV0SroN_QyAXnyOUANUImGhnprU6r60DyFmLX0-TADBdIDEUAMlf0oVg5ALgIWl5cwAtQGtw58GDRRSt-yMaPqfI76a3IWAvuykiBFvnWYa0Alu_1eoaNo2Q8h2wYR55069eJH7H8mLDWceQfenhlojEIALMKVH7okZZ55Y3IaB29X8ZIW5gFqqh71e3QFwSiewNX2mgzquVPQvD94piuIRUJXnCpt-TirgNOUu-2m7JTyhLOTn-0IRUJXnCe0nVrBzK9W6; isg=BA4OUU3c5aroylBlEjf8jyH2X-TQj9KJb7Qeijh1HpRJm4_14x7emesV08f3g8qh'
cookie = input("cookie:")

#获取搜索内容
serach_text = input("搜索内容:")
encoded_text = urllib.parse.quote(serach_text)

#js逆向，获取sign
eT = int(time.time() * 1000)
# eT = 1741592229028
eC = "12574478"

params = {"device": "HMA-AL00", "isBeta": "false", "grayHair": "false", "from": "nt_history", "brand": "HUAWEI",
          "info": "wifi", "index": "4", "rainbow": "", "schemaType": "auction", "elderHome": "false",
          "isEnterSrpSearch": "true", "newSearch": "false", "network": "wifi", "subtype": "",
          "hasPreposeFilter": "false", "prepositionVersion": "v2", "client_os": "Android", "gpsEnabled": "false",
          "searchDoorFrom": "srp", "debug_rerankNewOpenCard": "false", "homePageVersion": "v7",
          "searchElderHomeOpen": "false", "search_action": "initiative", "sugg": "_4_1", "sversion": "13.6",
          "style": "list", "ttid": "600000@taobao_pc_10.7.0", "needTabs": "true", "areaCode": "CN", "vm": "nw",
          "countryNum": "156", "m": "pc",
          #翻页控制
          "page": 1,
          "n": 48,
          #搜索关键词
          "q": encoded_text,
          "qSource": "url",
          "pageSource": "a21bo.jianhua/a.201856.d13", "tab": "all", "pageSize": "48", "totalPage": "71",
          "totalResults": "3392", "sourceS": "48", "sort": "_coefp", "bcoffset": "-16", "ntoffset": "6",
          "filterTag": "", "service": "", "prop": "", "loc": "",
          #价格区间
          "start_price": None, "end_price": None,
          "startPrice": None, "endPrice": None, "categoryp": "", "ha3Kvpairs": None,
          "myCNA": "9Gi/HqkZLQ4CAXFftyTryaKX"}

ep_data_1 = {
    "appId": "34385",
    "params": json.dumps(params)
}

ep_data_1 = json.dumps(ep_data_1).replace(" ", "")

string = em_token + "&" + str(eT) + "&" + eC + "&" + ep_data_1

MD5 = hashlib.md5()
MD5.update(string.encode('utf-8'))
sign = MD5.hexdigest()



#发送请求
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "cookie":cookie
        # cookie
        }
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
data = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": eT,
    "sign": sign,
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp11",
    "data": ep_data_1
}
response = requests.get(url, headers=headers, params=data)


#返回json处理，提取数据
json1 = re.search('mtopjsonp11\((.*)\)', response.text).group(1)
json_data = json.loads(json1)
list = json_data["data"]["itemsArray"]

#获取当日日期
now = datetime.now()
date_str = now.strftime('%Y-%m-%d')

filename = f'data_{date_str}_{serach_text}.csv'

with open(filename, 'a', newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "procity", "shopName"])
    writer.writeheader()
    for item in list:
        writer.writerow({"title": item["title"], "price": item["utLogMap"]["price"], "procity": item["procity"], "shopName": item["shopInfo"]["title"]})
