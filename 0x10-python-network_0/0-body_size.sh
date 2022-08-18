#!/usr/bin/python3
#Write a Bash script that takes in a URL
curl -s "$1" | wc -c
