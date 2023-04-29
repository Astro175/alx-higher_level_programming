#!/usr/bin/python3
"""Module that uses the request module for url"""
import requests


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    res = requests.get(url)

    print('Body response')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- type: {}'.format(res.text))
