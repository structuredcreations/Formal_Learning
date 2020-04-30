#test file (sum=2553)
#http://py4e-data.dr-chuck.net/comments_42.xml

#actual file (sum end with 4)
#http://py4e-data.dr-chuck.net/comments_351803.xml

import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/comments_351803.xml'
xml_text = urlopen(url, context=ctx).read()
#print(xml_text)


stuff = ET.fromstring(xml_text)
lst = stuff.findall('comments/comment')
print('Name count:', len(lst))

num_total=0

for item in lst:
    #print('Name', item.find('name').text)
    #print('Num_raw', item.find('count').text)
    num_total=int(item.find('count').text)+num_total
print('Grand Total is',num_total)

#python3 downloads/py4e/c3_w5_xml_total.py
