#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <year> <day>"
  echo "  <year>: The year for the Advent of Code challenge (e.g., 2023)"
  echo "  <day>: The day of the challenge (e.g., 01, 02, ..., 25)"
  exit 1
fi

# Extract year and day from arguments
year="$1"
day="$2"

# Construct the file path
input_file_path="$year/puzzle_input/$day"_input.txt
example_file_path="$year/puzzle_input/$day"_example.txt

# Create the "input" directory if it doesn't exist
mkdir -p "$year/puzzle_input"

# Check if the file exists
if [ -f "$input_file_path" ]; then
  rm "$input_file_path"
  echo "File '$input_file_path' already exists"
fi

touch "$example_file_path"

# Check if the boilerplate file exists
if [ ! -f "bp.py" ]; then
  echo "Error: bp.py not found."
  exit 1
fi

# solution file path
solution_file_path="$year/$day".py

# create year/day solution file
if [ ! -f "$solution_file_path" ]; then
  # Create the file (empty)
  touch "$solution_file_path"
fi
cp "bp.py" "$solution_file_path"

# Replace "20xx" with the actual year in the new file
sed -i "s/20xx/$year/g" "$solution_file_path"
sed -i "s/00/$day/g" "$solution_file_path"

# Execute the Python script
python3 setup.py $year $day $input_file_path