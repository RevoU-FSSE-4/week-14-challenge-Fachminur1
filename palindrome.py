# palindrome.py

def is_palindrome(string): 
    if string == string[::-1]: 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 

string = "racecar"

print(is_palindrome(string))