#!/usr/bin/python3
"""Module that gets a request header"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as feedback:
        header = feedback.getheader('X-Request-Id')
        print(header)
