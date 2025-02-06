#Write a Python function that takes 
# a list and returns a new list with
# unique elements of the first list. 
# Note: don't use collection set.


def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_list([1, 2, 3, 3, 2, 4, 5, 5])) 
# [1, 2, 3, 4, 5]