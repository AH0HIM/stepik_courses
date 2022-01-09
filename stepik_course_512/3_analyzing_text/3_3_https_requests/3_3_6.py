import requests
import re

url_a, url_b = input(), input()
flag = False


for url in re.findall(r'<a href="(.*)">', requests.get(url_a).text):
    if url_b in re.findall(r'<a href="(.*)">', requests.get(url).text):
        print('Yes')
    else:
        print('No')