import requests
import json
from flask import request
from keys import APIKEY
headers = {
    "Accept": "application/json",
    "X-Macys-Webservice-Client-Id": APIKEY,
}
url = 'http://api.macys.com/v4/catalog/search?searchphrase=red+dress'
resp = requests.get(url ,headers=headers);
jdata = json.loads(resp.text)

print json.dumps(jdata,sort_keys=True, indent=2) 