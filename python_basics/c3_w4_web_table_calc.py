
#test link (Sum=2553)
#http://py4e-data.dr-chuck.net/comments_42.html

#actual link (Sum ends with 43)
#http://py4e-data.dr-chuck.net/comments_351801.html


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/comments_351801.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

y=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    x = int(tag.contents[0])
    y=x+y

print(y)


#python3 downloads/py4e/c3_w4_web_table_calc.py
