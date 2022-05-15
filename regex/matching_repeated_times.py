#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
#For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.

import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*?[Aa]", text) 
  
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#there is a substantial performance difference that will certainly become apparent on larger inputs.
#The greedy * tells the engine to try to match the longest stretch possible, which means that the matcher will walk all the way to the end of the string 
#(since every character matches .)
#and then keep backtracking until it finds the second a or A within things that already matched.
#For this case you could use .*?, but a good habit: make adjacent tokens mutually exclusive.
#To clarify further: 
# '[^aA]*' examines/matches the fewest characters and has zero backtracking.
# '.*?' examines/matches the fewest characters and has backtracking for every character between the first and second "a".
# '.*' examines all characters and has backtracking for every character after the last "a"

print(re.search(r"Py.*n", "Pygemalion"))
#returns Pygmalion

print(re.search(r"Py.*n", "Python Programming"))
#returns Python programmin - Greedy

print(re.search(r"Py[a-z]*n", "Python Programming"))
#returns python


#return a match with one or mores 
print(re.search(r"o+l+", "woollies"))
#returns "ooll" 

