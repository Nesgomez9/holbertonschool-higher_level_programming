#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -sI "$1" | awk /Content-Length:/ | cut -d " " -f 2
