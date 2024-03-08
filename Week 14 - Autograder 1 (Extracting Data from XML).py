# https://www.py4e.com/code3/geoxml.py?PHPSESSID=0054294d206776b7db2e6804748ac576
# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1907332.xml

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Address: ')
html = urlopen(url, context=ctx).read()
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')

count = 0
for item in lst:
    numbers = int(item.find('count').text)
    count = numbers + count

print(count)

