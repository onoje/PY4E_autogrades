# https://www.py4e.com/code3/urllink2.py?PHPSESSID=fadaa9b9b8d88f41b6bd413adb4c7f27
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1907330.html

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
count = 0
tags = soup('span')
for tag in tags:
    content = tag.contents[0]
    try:
        number = int(content)
        total = total + number
        count = count + 1
    except:
        continue

print("Count", count)
print("Sum", total)
