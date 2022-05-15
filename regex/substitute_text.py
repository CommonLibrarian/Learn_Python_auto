import re
def transform_comments(line_of_code):
  result = re.sub(r"##*", r"//", line_of_code) # r"##*" asterisk allowing repetition of such text to be found
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
