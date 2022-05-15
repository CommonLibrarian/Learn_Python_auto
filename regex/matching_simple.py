import re

print(re.search(r"aza", "plAzA", re.IGNORCASE))

#or

print(re.search(r"b.ng", "bongaricious"))

#or

print(re.search(r"[a-z]way", "highway"))

#or

print(re.search(r"[a-zA-Z0-9]","cloud9"))

#or

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

#match anything except ~ "^" (circumflex)
#matchi anything that is not a letter
print(re.search(r"[^a-zA-Z]", "this is a sentence with spaces"))
#returns the first space at this string

#if we put a 'space' in the return except the following argument /

print(re.search(r"[^a-zA-Z ]", "this is a sentence with spaces."))
#returns period sign at the end of the string

#match 1 or more by using the pipe command
print(re.search(r"dog|cat". "I like dogs."))
#regex only find one item at a time... such as this example
print(re.search(r"dog|cat". "I like dogs and cats.")) #only returns cats

#to find everything... re.findall
print(re.findall(r"dog|cat". "I like dogs and cats."))

#returns ['dog', 'cat']
