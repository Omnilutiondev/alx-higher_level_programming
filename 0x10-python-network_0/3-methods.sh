#!/bin/bash
# The script takes in a URL and displays all the server HTTP methods
curl -sI "$1"| grep "Allow"| cut -d " " -f 2-
