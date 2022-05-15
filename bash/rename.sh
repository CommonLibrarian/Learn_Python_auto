#!/bin/bash

for file in *.TXT; do
  name=$(basename "$file" .TXT)
  mv "$file" "$name.txt"
done
