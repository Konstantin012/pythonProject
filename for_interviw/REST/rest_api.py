import pytest
import requests
import json

user_name="kkon870@gmail.com"
password="1324576890дущтП"
cred={user_name:password}
url="https://github.com/login"
url2="https://github.com/Konstantin012/QUOD"
cook = requests.get(url).cookies

r = requests.post(url,cred,cookies =cook)
print(r.status_code)
# r2=requests.get(url,cookies=cook)
# print(r2.text)