import re

#evil example
#circumflex indicating we want to start from the beginning, characters with under or uppercase and '_' underscore, and 
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$
#apply this pattern
print(re.search(pattern, "_this_is_a_valid_variable_name"))


print(re.search(r"A.*a", "Argentina")) #to match A to a everything end of the line character
#'Argentina'

print(re.search(r"^A.*a$", "Azerbaijan"))
#none

print(re.search(r"^A.*a$", "Australia"))
#'Australia'

