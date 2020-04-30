#test file (sum=2553)
#http://py4e-data.dr-chuck.net/comments_42.json

#actual file (sum end with 38)
#http://py4e-data.dr-chuck.net/comments_351804.json


from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = input('Enter - ')
#url='http://py4e-data.dr-chuck.net/comments_42.json'
url='http://py4e-data.dr-chuck.net/comments_351804.json'
JSON_text = urlopen(url, context=ctx).read()
#print(JSON_text)

data = json.loads(JSON_text)
print('User count:', len(data))

print('Name:', data["comments"])

dict=data["comments"]

data_total = 0

for item in dict:
#   print(item)
    print('Name:', item["name"])
    print('Number',item["count"])
    data_total = data_total + int(item["count"])


print('Grand Total is',data_total)

#python3 downloads/py4e/c3_w6_JSON_total.py
