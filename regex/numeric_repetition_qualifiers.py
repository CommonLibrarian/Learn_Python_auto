impore re

print(re.search(r"[a-zA-Z]{7}" , "Text"))
#text matching 7characters in total

print(re.findall(r"[a-zA-Z]{5}", "text"))
#matching characters of 7, everything in the text

print(re.findall(r"\b[a-zA-Z]{6}\b", "text"))
#find every text that contains 6 characters (whole word)


#We said that we can also have two numbers in the range. 
#For example, if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.
#in translation, find everything with at least 4 characters to the maximum of 10 characters inside the "text"
print(re.findall(r"\w{4,10}", "text"))


#a comma followed by a number means from zero up to that amount of repetitions. 
print(re.findall(r"s\w{,20}", "text"))

#or

print(re.findall(r"\b\w{,6}\b", "text"))
#find everyt whole-word with at least 6 repeated characters.
