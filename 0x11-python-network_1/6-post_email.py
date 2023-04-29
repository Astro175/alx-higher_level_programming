#!/usr/bin/python3
"""Module that makes a post request
   with requests module
"""
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)

    print(response.text)
