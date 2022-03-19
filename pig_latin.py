def pig_latin(text):
  words = text.split()
  new_words = []

  for word in words:
    if word.isalpha():
      new_word = word [1:] + word[0] + "ay"
      new_words.append(new_word)
    else:
      new_words.append(word)
  
  return " ".join(new_words)

		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
