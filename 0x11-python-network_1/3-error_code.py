#!/usr/bin/python3
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    request = Request(argv[1])
    try:
        with urlopen(request) as html:
            print(html.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
