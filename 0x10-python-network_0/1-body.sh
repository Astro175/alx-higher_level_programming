#!/bin/bash
# Curl sends a get method and prints the status
curl -s "$1" | sed -n '/HTTP\/1.1 200 OK/,$p'
