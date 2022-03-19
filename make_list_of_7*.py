#create multiples of seven by FOR LOOP
multiples = []
for x in range(1,11):
  multiples.append(x*7)
  
print(multiples)

#alternative
multiples = [ x*7 for x in range(1,11) ]
print(multiples)
