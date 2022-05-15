#!/bin/bash

###find file containing " jane " and test if they exists, and append the result to oldFiles.txt
grep " jane " ../data/list.txt | cut -d ' ' -f 3 > tempFile.txt
files=$(<tempFile.txt)
for i in $files ; do
 if test -e "..$i"; then echo "$i" >> oldFiles.txt;
 fi
done
