#!/bin/bash
# This script takes in a URL as an arg, sends a GET request to it, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
