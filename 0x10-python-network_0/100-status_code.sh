#!/bin/bash
#Script that returns the status code of a web server
curl -s -o /dev/null -w %{http_code} "$1"
