#!/usr/bin/env python3

# Take URLs in on std in and (when a response is received) output the url and the "final destination" after redirects have been followed

import sys
import requests
import threading
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def getRequest(url):
    try:
        response = requests.get(url, timeout=10, verify = False)
        if response.url:
            print (url + "|" + response.url.rstrip("/"))
    except Exception:
        pass

urls = []
for line in sys.stdin:
    urls.append(line.rstrip())

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(getRequest, urls)
