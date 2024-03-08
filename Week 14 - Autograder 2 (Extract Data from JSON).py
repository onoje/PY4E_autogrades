# https://www.py4e.com/code3/json2.py?PHPSESSID=8c56a5efa0f0856814704428007910a1
# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1907333.json
# https://www.py4e.com/code3/geoxml.py?PHPSESSID=8c56a5efa0f0856814704428007910a1

import json
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = input('Enter Address: ')
html = urlopen(data, context=ctx).read().decode('utf-8')
info = json.loads(html)

in_comments = info['comments']

total = 0
for item in in_comments:
    numbers = int(item['count'])
    total = total + numbers

print(total)
