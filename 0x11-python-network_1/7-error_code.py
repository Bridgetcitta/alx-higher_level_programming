#!/usr/bin/python3
"""A Python script that displays the body of the response."""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    fetched = requests.get(url)
    if fetched.status_code >= 400:
        print("Error code: {}".format(fetched.status_code))
    else:
        print(fetched.text)
