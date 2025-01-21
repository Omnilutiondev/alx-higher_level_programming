#!/bin/bash
# This script sends a request to a URL passed as an arg, and displays the status code of the response only.
curl -s -o /dev/null -w "%{http_code}" "$1"
