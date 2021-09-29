#!/usr/bin/env python3

# Take URLs in on std in and (when a response is received) follow redirects
# only outputting the original URL if the redirect finishes on a different domain.

import sys
import requests
import threading
import concurrent.futures

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def cleanURL(url):
    url = url.lower()
    url = url.removeprefix('http://')
    url = url.removeprefix('https://')
    if '/' in url:
        url = url[0:url.find('/')]
    if '?' in url:
        url = url[0:url.find('?')]
    return url

def getRequest(url):
    try:
        response = requests.get(url, timeout=10, verify = False)
        if response:
            # If original domain is not the same as redirected domain, print url
            # unless the only change is the addition of 'www.'
            if cleanURL(url) != cleanURL(response.url):
                if 'www.' + cleanURL(url) != cleanURL(response.url):
                    print(url)
    except Exception:
        pass

urls = []
for line in sys.stdin:
    urls.append(line.rstrip())

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(getRequest, urls)
