#!/usr/bin/env python
# coding:utf-8

import urllib
import json

url = "http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1517815457448"
url2 = "http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1517815457448"
data = urllib.urlopen(url).read()
data = data.decode('UTF-8')
json_str = json.loads(data)
print data
print json_str

for i in json_str["returndata"]["datanodes"]:
    print i["code"][3:12]
    print i["data"]["strdata"]

