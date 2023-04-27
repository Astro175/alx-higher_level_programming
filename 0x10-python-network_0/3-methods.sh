#!/bin/bash
# Script that uses curl to see available options
curl -sI "$1" | grep "allow" | sed 's/Allow: //g'
