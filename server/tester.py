import requests
import json
from flask import request
from keys import APIKEY

#returns top 5 picurls/producturl/producttitle for the designated keywords
#def macySearch(key):
headers = {
    "Accept": "application/json",
    "X-Macys-Webservice-Client-Id": APIKEY,
}
url = 'http://api.macys.com/v4/catalog/search?searchphrase=red+dress&show=product&perpage=5&imagewidth=262&avoidredirects=true'
resp = requests.get(url ,headers=headers);
print resp.status_code
jdata = json.loads(resp.text)

num_products = jdata["searchresultgroups"][0]["totalproducts"]
print "Number of products is: " + str(num_products)
if num_products == 0:
    print None

products = jdata["searchresultgroups"][0]["products"]['product']

retArr = range(15)

k = 0
for i in products:
    retArr[k] = i["summary"]["name"]
    k += 1
    retArr[k] = i["summary"]["producturl"]
    k += 1
    retArr[k] = i["image"][0]["imageurl"]
    k += 1
    print "\n\n"
    
