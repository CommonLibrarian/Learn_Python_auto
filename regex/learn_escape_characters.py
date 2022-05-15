#thi is a WRONG asnwer
import re

def check_sentence(text):       
   result = re.search(r"^[A-Z]+[a-z]+[\s]+[a-z]+[\.!\?]$", text)
   return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#TRACEBACK

#my current regex doesn't work because it tries to look for

^[A-Z]+[a-z]+[\s]+[a-z]+[\.!\?]$

^[A-Z]+: One or more capital letters at the start of the string
[a-z]+: One or more small letters after the capital letters
[\s]+: One or more whitespaces after the small letters
[a-z]+: One or more small letters after the spaces
[\.!\?]+$: One or more of the punctuations (., !, or ?) after the second run of small letters, and then the string ends.

What I actually want to do:

^[A-Z][A-Za-z\s]+[\.!\?]$

^[A-Z]: Exactly one capital letter at the start of the string
[A-Za-z\s]+: One or more capital letters / small letters / spaces
[\.!\?]$: One punctuation mark at the end of the string
  
 #RIGHT answser
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][A-Za-z\s]+[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
