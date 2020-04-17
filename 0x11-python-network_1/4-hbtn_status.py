#!/usr/bin/python3
from requests import get


if __name__ == "__main__":
    response = get("https://intranet.hbtn.io/status")
    html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
