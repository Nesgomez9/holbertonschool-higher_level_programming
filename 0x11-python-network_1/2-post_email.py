#!/usr/bin/python3
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    data = urlencode({"email": argv[2]})
    data = data.encode("ascii")
    request = Request(argv[1], data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
