#!/bin/bash
# Bash Script that takes in a url and returns the body size
curl -s "$1" | wc -c
