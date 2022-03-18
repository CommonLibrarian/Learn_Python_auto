#he is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
    new_string = input_string.split()
    new_string = "".join(new_string).lower()
    reverse_string = new_string[::-1]    
    
    if new_string == reverse_string:
        return True
    else:
        return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
