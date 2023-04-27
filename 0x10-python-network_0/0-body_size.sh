#!/bin/bash

# Bash Script that takes in a url and returns the body size

if [ $# -eq 1 ]; then

	if ! echo "$1" | grep -q "://"; then

		url="http://$1"

	else

		url="$1"

	fi

	size=$(curl -s "$url" | wc -c)

	echo "$size"

fi

