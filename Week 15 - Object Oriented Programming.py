# http://www.py4e.com/code3/party1.py
# http://www.py4e.com/code3/elev.py
# http://www.py4e.com/code3/urllinks.py
# https://docs.python.org/3/library/html.parser.html
# http://www.py4e.com/code3/party2.py
# http://www.py4e.com/code3/party3.py
# http://www.py4e.com/code3/party4.py
# http://www.py4e.com/code3/party5.py
# http://www.py4e.com/code3/party6.py


"""
stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))
# the __getitem__ method in the list class and pass the list and the item we want retrieved from the list as parameters.

stuff = list()
print(dir(stuff))
"""


"""
usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non-US Floor Number is', wf)
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
class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
"""


"""
class PartyAnimal:
    x = 0  # x => attribute

    def party(self):  # party => method
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()  # the first executable line of code
# This is where we instruct Python to construct an object or instance of the class PartyAnimal.

an.party()
an.party()
an.party()
PartyAnimal.party(an)
"""


"""
class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))
"""


"""
class PartyAnimal:
    def __init__(self):  # constructs our object  # came from initial
        self.x = 0
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):  # destructed our object
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
"""


"""
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')
j.party()
s.party()
# the output of the program shows that each of the objects (s and j) contain their own independent copies of x and nam.
"""


# from party import PartyAnimal
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


class CricketFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
