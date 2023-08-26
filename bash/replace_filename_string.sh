#!/bin/bash

# Prompt the user
read -p "Enter the old value: " old_word
read -p "Enter the new value: " new_word
read -p "Enter the directory: " directory
read -p "Do you want check subfolders? (y/n): " recursive_choice

# Find and rename files in the specified directory
function rename_files() {
  local dir="$1"
  for filename in "$dir"/*; do
    if [[ -f "$filename" ]]; then
      base=$(basename "$filename")
      ext="${base##*.}"
      base_without_ext="${base%.*}"

      if [[ $base_without_ext == *"$old_word"* ]]; then
        new_base=$(echo "$base_without_ext" | sed "s/$old_word/$new_word/g")
        
        if [[ -n "$ext" && "$base_without_ext" != "$ext" ]]; then
          new_filename="$new_base.$ext"
        else
          new_filename="$new_base"
        fi
        
        mv "$filename" "$dir/$new_filename"
      fi
    elif [[ -d "$filename" && $recursive_choice == "y" ]]; then
      rename_files "$filename"
    fi
  done  
}

rename_files "$directory"

