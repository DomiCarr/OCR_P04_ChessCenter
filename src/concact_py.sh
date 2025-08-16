#!/bin/bash

# Output file
output_file="all_python_files.txt"

# Empty the output file if it exists
> "$output_file"

# Find all .py files in the current directory and subdirectories
find . -type f -name "*.py" | while read pyfile; do
    echo "----------------------------------------" >> "$output_file"
    echo "File: $pyfile" >> "$output_file"
    echo "----------------------------------------" >> "$output_file"
    cat "$pyfile" >> "$output_file"
    echo -e "\n\n" >> "$output_file"
done

echo "All Python files have been written to $output_file"