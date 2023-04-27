#!/bin/bash
# Script that uses curl to see available options
curl -sI "$1" | grep "Allow" | sed 's/Allow: //g'
