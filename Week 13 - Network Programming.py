# https://www.w3.org/Protocols/rfc2616/rfc2616.txt
# http://www.pr4e.org/
# http://data.pr4e.org/romeo.txt
# http://www.py4e.com/code3/socket1.py
# http://www.pr4e.com/
# http://data.pr4e.org/cover3.jpg
# http://www.py4e.com/code3/urljpeg.py
# http://www.py4e.com/code3/urllib1.py
# http://www.py4e.com/code3/urlwords.py
# http://www.py4e.com/code3/curl1.py
# http://www.py4e.com/code3/curl2.py
# http://www.py4e.com/code3/urlregex.py
# https://docs.python.org/
# https://pypi.python.org/pypi/beautifulsoup4
# https://packaging.python.org/tutorials/installing-packages/
# http://www.py4e.com/code3/bs4.zip
# http://www.py4e.com/code3/urllink2.py
# http://www.dr-chuck.com/page1.htm
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# http://www.py4e.com/cover.jpg
# http://www.py4e.com/code3


"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# the encode() and decode() methods convert strings into bytes objects and back again
mysock.send(cmd)

while True:
    data = mysock.recv(512)  # receives data in 512-character  # recv() returns an empty string
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
"""


"""
print(b'Hello world')
print('Hello world'.encode())
# encode() and b'' are equivalent (different notation)
"""


"""
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)  # delay  # with delay we can receive more data at once.
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
"""


"""
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# the web page has been opened with urllib.request.urlopen, we can treat it like a file
for line in fhand:  # for loop can use with urllib
    print(line.decode().strip())
"""


"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""

"""
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')  # the wb argument for open() opens a binary file for writing only. 
fhand.write(img)
fhand.close()
"""


"""
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
"""


"""
# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl  # the ssl library allows this program to access websites that strictly enforce HTTPS.


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
# The read method returns HTML source code as a bytes object instead of returning an HTTPResponse object.
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
"""


"""
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
"""


"""
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
"""
