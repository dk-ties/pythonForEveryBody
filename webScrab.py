# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
sum = 0


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

def nextUrl(url):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup


""" # Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    sum += int(tag.contents[0])
    
print('Sum is: ', sum)
 """
def runTheSoup(soup):
    # Retrieve all of the anchor tags
    tagCount = 0
    tags = soup('a')
    for tag in tags:
        tagCount += 1
        if tagCount == 18:
            
            return tag.get('href', None)

def digIn(rounds):
    runs = 0
    target = ''
    if target == '':
        target = url
    while runs < rounds:
        print(runTheSoup(nextUrl(target)))
        target=runTheSoup(nextUrl(target))
        runs += 1
        
    return target
        

digIn(7)
 
 
 
 
 
 
        
"""  print('We are at a new HP now')
        newTag = nextUrl(tag.get('href', None))
        tagCount = 0
        for tag in newTag('a'):
            tagCount += 1
            print(tag.get('href', None))
            if tagCount == 4:
                print('We are at a new HP now')
                newTag = nextUrl(tag.get('href', None))
                tagCount = 0

 """