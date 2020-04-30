#test link (Sum=2553)
#http://py4e-data.dr-chuck.net/known_by_Fikret.html

#actual link (Sum ends with 43)
#http://py4e-data.dr-chuck.net/known_by_Carri.html

extract_url_num = 18
number_of_Loops = 7


#starting_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#starting_url = 'http://py4e-data.dr-chuck.net/known_by_Montgomery.html'
#starting_url = 'http://py4e-data.dr-chuck.net/known_by_Mhairade.html'
#starting_url = 'http://py4e-data.dr-chuck.net/known_by_Butchi.html'
starting_url = 'http://py4e-data.dr-chuck.net/known_by_Carri.html'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while number_of_Loops>0:
    #print('start_of_loop_url',starting_url)
    html = urlopen(starting_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    position = 0;

    tags = soup('a')
    for tag in tags:
        position=position+1
        url_at_select_line=tag.get('href', None)
        if position==extract_url_num:
            #print('POS:',position,'URL:', tag.get('href', None))
            print('new starting url',url_at_select_line)
            break
            starting_url = url_at_select_line
    number_of_Loops=number_of_Loops-1
    starting_url = url_at_select_line

print('end of run')


#python3 downloads/py4e/c3_w4_webpage_link_crawler_full.py
