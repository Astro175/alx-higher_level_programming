#!/bin/bash
# Script that uses curl to pass a header variable
curl -sH "X-School-User-Id: 98" "$1"
