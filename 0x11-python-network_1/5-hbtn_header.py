#!/usr/bin/python3
"""
A Python script that displays the value of the variable X-Request-Id
in the response header
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    fetched = requests.get(url)
    print(fetched.headers.get("X-Request-Id"))
