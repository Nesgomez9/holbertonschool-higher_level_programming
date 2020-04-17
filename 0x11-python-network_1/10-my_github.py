#!/usr/bin/python3
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    request = get(url, auth=(argv[1], argv[2]))
    js = request.json()
    print(js.get("id"))
