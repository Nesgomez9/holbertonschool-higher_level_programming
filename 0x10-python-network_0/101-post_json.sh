#!/bin/bash
#Script that returns body of a post with jason content
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
