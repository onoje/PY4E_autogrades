# https://www.py4e.com/code3/opengeo.py?PHPSESSID=83d720af5981b90a186c525a8b925bb4
# http://py4e-data.dr-chuck.net/opengeo?

import urllib.request, urllib.parse
import json, ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

address = address.strip()
parms = dict()
parms['q'] = address

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)

print(js['features'][0]['properties']['plus_code'])




