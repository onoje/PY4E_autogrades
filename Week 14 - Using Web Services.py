# http://www.json.org/
# http://www.py4e.com/code3/xml1.py
# http://www.py4e.com/code3/xml2.py
# http://www.py4e.com/code3/json2.py
# http://www.oauth.net/


"""
import xml.etree.ElementTree as ET
# using ElementTree allows us to extract data from XML without worrying about the rules of XML syntax.

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)  # fromstring converts the string representation of the XML into a “tree” of XML elements.
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
"""


"""
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
# findall method retrieves a Python list of subtrees that represent the user structures in the XML tree.
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
"""


"""
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)

lst = stuff.findall('users/user')
print('User count:', len(lst))

lst2 = stuff.findall('user')
print('User count:', len(lst2))
"""



import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
# json.loads() is Python list which we traverse with a for loop, and each item within that list is a Python dictionary.
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])



