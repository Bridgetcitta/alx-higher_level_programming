#!/usr/bin/python3
"""A Python script that displays the body of the response."""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    getattrib = {"email": sys.argv[2]}

    fetched = requests.post(url, data=getattrib)
    print(fetched.text)
