#!/usr/bin/python3
from requests import post
from sys import argv


if __name__ == "__main__":
    response = post(argv[1], {"email": argv[2]})
    print(response.text)
