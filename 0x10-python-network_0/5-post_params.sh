#!/bin/bash
# SCript that uses curl post method
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
