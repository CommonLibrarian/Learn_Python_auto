import os

print(re.search(r".com", "welcome"))
#'lcome'
print(re.search(r"\.com", "welcome"))
#none
print(re.search(r"\.com", "mydomain.com"))
#'.com'

print(re.search(r"\w*". "and_this_is_antoher"))

#evil example

import re
def check_character_groups(text):
  result = re.search(r"\b\w+\s+\w+\b", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
