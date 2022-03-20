file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

#.items() function make tuples of "keys" : and "value" 
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext)) #.format order is reversed due to the declaring order

#testing what i learned

file_counts.keys()
file_counts.values()

for value in file_counts.vlaues():
  print(value)
  


