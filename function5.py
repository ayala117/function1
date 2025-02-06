#Write a function that accepts string 
# from user and print all permutations of 
# that string.
123
from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

# Example usage
s = input("Enter a string: ")
print_permutations(s)

#output  123 -123  132  213 231  312  321