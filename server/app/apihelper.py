import requests
import json
from flask import request
from app import app
from keys import APIKEY

#returns top 5 picurls/producturl/producttitle for the designated keyword
def macy_search(key):
    hdr = {
        "Accept": "application/json",
        "X-Macys-Webservice-Client-Id": APIKEY,
    }
    
    
    url = 'http://api.macys.com/v4/catalog/search?searchphrase=' + key[0] + '&show=product&perpage=5&imagewidth=262&avoidredirects=true'
    resp = requests.get(url ,headers=hdr)
    app.logger.debug(resp.status_code)
    jdata = json.loads(resp.text)
    
    print jdata
    if "searchresultgroups" in jdata:
            num_products = jdata["searchresultgroups"][0]["totalproducts"]
            app.logger.debug(num_products)
            if num_products == 0:
                return None
            
            products = jdata["searchresultgroups"][0]["products"]['product']
            
            retArr = [None]*16
            retArr[0] = num_products;
            k = 1
            for i in products:
                retArr[k] = i["summary"]["name"]
                k += 1
                retArr[k] = i["summary"]["producturl"]
                k += 1
                retArr[k] = i["image"][0]["imageurl"]
                k += 1
            return retArr
    return None
            
    
    
    
