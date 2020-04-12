#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
