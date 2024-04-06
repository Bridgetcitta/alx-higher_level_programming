#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    fetched = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(fetched.text)))
    print("\t- content: {}".format(fetched.text))
