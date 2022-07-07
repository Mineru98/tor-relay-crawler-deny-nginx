# -*- coding:utf-8 -*-
import re
import requests

res = requests.get("https://check.torproject.org/exit-addresses")
for row in res.text.split("\n"):
    if row.find("ExitAddress") != -1:
        ipList = re.findall("[0-9]+(?:\.[0-9]+){3}", row)
        print(ipList[0])
