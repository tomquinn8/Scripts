#!/usr/bin/env python3

# Take URLs in on std in and (when a response is received) output the url, the response code and in the case of 30x redirects, the Location header

import sys
import requests
import threading
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def getRequest(url):
    try:
        response = requests.get(url, timeout=10, verify = False, allow_redirects=False)
        if response:
            redirect = '|' + str(response.headers['Location']) if '30' in str(response.status_code) else ''
            print (url + '|' + str(response.status_code) + redirect)
    except Exception:
        pass

urls = []
for line in sys.stdin:
    urls.append(line.rstrip())

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(getRequest, urls)
