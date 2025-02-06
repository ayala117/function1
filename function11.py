#Write a Python function that checks
# whether a word or phrase is palindrome or
# not. Note: A palindrome is word, phrase,
# or sequence that reads the same backward 
# as forward, e.g., madam

def is_palindrome(word):
    word = word.replace(" ", "").lower()  # Ignore spaces and make lowercase
    return word == word[::-1]

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A Santa at NASA"))  # true