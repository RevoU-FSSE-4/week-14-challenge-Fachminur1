# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    pass
def is_palindrome(string): 
    if string == string[::-1]: 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 

# You can test your function with print statements below
# Example:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))  # Expected output: False
string = "racecar"

print(is_palindrome(string))