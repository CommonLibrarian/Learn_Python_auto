import re
log = "July 31 07:51:32 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"

#the first \ and [ literally means which is used as the escape character.
#This means that the next character, which is a square bracket here, is treated literally for matching purposes. 
regex = r"\[(\d+)\]"
#After the square bracket, comes the first parentheses. Since it isn't escaped, we know it'll be used as a capturing group. 
#The capturing group parentheses are wrapping the backslash d+ symbols.
#we know that this expression will match one or more numerical characters.
#After the closing parentheses of the capturing group, we have the closing square bracket symbol, also proceeded by the escape character.
#After calling the search function, we know that because we're capturing groups in an expression, /n
#we can access the matching data by accessing the value at index 1. 
result = re.search(regex, log)
print(result[1])

#prints 12345

#extract PID here

def extract_pid(log_line):
  regex = r"\[(\d+)]"
  result = re.search(regex, log_line)
  if result is None:
    return ""
  return result[1]

print(extract_pid("99 elephants in a[cage]"))

#evil example
import re 
def extract_pid(log_line):
     regex = r"\[(\d+)\]\: ([A-Z]*)"
     result = re.search(regex, log_line)
     if result is None:
         return None
     return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
