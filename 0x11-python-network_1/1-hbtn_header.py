#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info().get("X-Request-Id"))
