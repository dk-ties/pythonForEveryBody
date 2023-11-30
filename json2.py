import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inputUrl = input('Enter a URL ')
if len(inputUrl) < 1:
    inputUrl= 'http://py4e-data.dr-chuck.net/comments_42.json'




#url = serviceurl + urllib.parse.urlencode(parms) 
url = inputUrl
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
#data = data.decode()
print('Retrieved', len(data), 'characters')
#print(data.decode())



info = json.loads(data)
print('User count:', len(info['comments']))
sum = 0
for item in info['comments']:
    sum += int(item['count'])

print('Total sum is', sum)
