#test link (Sum=2553)
#http://py4e-data.dr-chuck.net/known_by_Fikret.html

#actual link (Sum ends with 43)
#http://py4e-data.dr-chuck.net/known_by_Carri.html

extract_url_num = 3


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0;

tags = soup('a')
for tag in tags:
    position=position+1
    if position==extract_url_num: break
print('URL:', tag.get('href', None))


#print(x)






#python3 downloads/py4e/c3_w4_webpage_link_crawler.py
