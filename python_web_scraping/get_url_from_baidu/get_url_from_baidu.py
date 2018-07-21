import requests
import json
import re

headers = {
   "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
}

url = "http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true"
files = {
   'file':open("test.png","rb")
}
temp_data = json.loads(requests.post(url=url,headers=headers,files=files).text)
#print(temp_data)

ans_url = "http://image.baidu.com/pcdutu/p_list?queryImageUrl=" + str(temp_data['url']) + "&querySign" + temp_data["querySign"] + "&simid=0,0"
#print(ans_url)
page_source= requests.get(url=ans_url,headers=headers).text

str_page_source = str(page_source)
print(str_page_source)
result_url = re.findall(r"\"fromURL\":\"(.+?)\",\"",str_page_source)

file = open("result.txt",'w')
for item in result_url:
    file.write(repr(item.strip("\'")))
file.close()
