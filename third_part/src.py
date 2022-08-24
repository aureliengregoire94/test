from itertools import product
import requests
import json
import gzip

def http_request():
    load = {}
    load['isadmin'] = 1
    r = requests.get('https://httpbin.org/anything', headers = {"User-Agent":"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    return r.content


class question2:
    def __init__(self):
        f = gzip.open("third_part/data/data.json.gz", "r")
        data = f.read()
        self.dict = json.loads(data.decode('utf-8'))

    def product_print(self):
        for i in self.dict['Bundles']:
            print(i['Product'][0]['Name'], ":", i['Product'][0]['Price'])

newobj = question2()
for i in newobj.dict: 
    print(i)
print(newobj.dict['Bundles'][0]['Product'])