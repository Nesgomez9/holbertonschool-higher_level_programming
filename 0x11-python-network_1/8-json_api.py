#!/usr/bin/python3
from requests import post
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    try:
        request = post(url, data)
        js = request.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}" .format(js.get("id"), js.get("name")))
    except:
        print("Not a valid JSON")
