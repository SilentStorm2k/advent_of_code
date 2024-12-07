#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <year 20XX> <day 01,..,25>"
  exit 1
fi

# Extract year and day from arguments
year="$1"
day="$2"

# Construct the file path
file_path="$year/$day.py"

# Check if the file exists
if [ ! -f "$file_path" ]; then
  echo "Error: File '$file_path' does not exist."
  exit 1
fi

# Execute the Python script
python3 "$file_path"