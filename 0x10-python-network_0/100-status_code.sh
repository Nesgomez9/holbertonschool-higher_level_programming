#!/bin/bash
#Script that returns the status code of a web server
URL=$1
RESPONSE=$(curl --write-out %{http_code} --silent --output /dev/null ${URL})
