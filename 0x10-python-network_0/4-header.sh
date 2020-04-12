#!/bin/bash
# take a URL, send a request to that URL, and display the size of the body of the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
