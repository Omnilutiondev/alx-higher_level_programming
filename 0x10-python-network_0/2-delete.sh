#!/bin/bash
# This script sends a DELETE request to the URL passed as the first arg and displays the response
curl -sX "DELETE" "$1" 
