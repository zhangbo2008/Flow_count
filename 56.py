'''

继续写刷流量代码
GET bb.spider668.com/?s=home-index-cnzz&agency_name=bb&token=vxaK1vDGaCm4 HTTP/1.1




POST http://bb.spider668.com/?s=/home-index-request_ip.html HTTP/1.1
Host: bb.spider668.com
Connection: keep-alive
Content-Length: 0
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://bb.spider668.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36 MMWEBID/3882 MicroMessenger/7.0.9.1560(0x2700099B) Process/tools NetType/WIFI Language/zh_CN ABI/arm64
Referer: http://bb.spider668.com/?s=home-index-cnzz&agency_name=bb&token=WX23tTWe4bU1Th8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-CN;q=0.9,en-US;q=0.8
Cookie: waf_cookie=7407cc52-83f0-46a59774dbe857ec9d81549ab061771ac080; PHPSESSID=fnhqpvpb18glhal0eskc6surd5; UM_distinctid=171743bd58f1ad-0f254c4742780c-4126631b-42cc0-171743bd590c; CNZZDATA1277912465=1621950246-1586792588-null%7C1586792588; CNZZDATA1278167971=1889505800-1586790338-null%7C1586790338; CNZZDATA1278308062=1267381255-1586787680-null%7C1586788621











'''


import requests

import requests

kw = {'wd': '长城'}

headers = {     'Connection': 'keep - alive',
'Accept - Encoding': 'gzip, deflate',
'Accept - Language': 'zh - CN, en - US',
'q' : '0.9',
'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-AL10 Build/HONORBKK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36 MMWEBID/3882 MicroMessenger/7.0.9.1560(0x2700099B) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'

}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/")
response = requests.get("http://bb.spider668.com/?s=home-index-cnzz&agency_name=bb&token=vxaK1vDGaCm4 ")

cookiesDit = {
'waf_cookie':'7407cc52-83f0-46a59774dbe857ec9d81549ab061771ac080','PHPSESSID':'fnhqpvpb18glhal0eskc6surd5', 'UM_distinctid':'171743bd58f1ad-0f254c4742780c-4126631b-42cc0-171743bd590c', 'CNZZDATA1277912465':'1621950246-1586792588-null%7C1586792588', 'CNZZDATA1278167971':'1889505800-1586790338-null%7C1586790338', 'CNZZDATA1278308062':'1267381255-1586787680-null%7C1586788621'
}
postData={'s':'/home-index-request_ip.html'}
response = requests.post('http://bb.spider668.com/',data = postData,headers=headers,cookies=cookiesDit,verify=False)

# 查看响应内容，response.text 返回的是Unicode格式的数据



response = requests.get("http://bb.spider668.com/?s=home-index-cnzz&agency_name=bb&token=vxaK1vDGaCm4%20", headers=headers)



print(response.text)
