#!/bin/bash

# A Bash script that:
    # takes in a URL,
    # sends a GET request to the URL,
    # displays the body of the response.
# Display only body of a 200 status code response
# Use curl
curl -sfL "$1" -X GET