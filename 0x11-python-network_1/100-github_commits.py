#!/usr/bin/python3
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    request = get(url)
    js = request.json()
    for info in js[:10]:
        commit = info.get("commit")
        author = commit.get("author")
        print("{}: {}".format(info.get("sha"), author.get("name")))
