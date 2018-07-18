# Write a function to check if a string is a permutation of a palindrome of another string,
# a palindrome is a string that is the same backwards and forwards: Hannah <==> Hannah. 
# A permutation of a the palindrome "Hannah" would be "Hnnaha"

# Problem clairification: Essentially a check on if the string is a palindrome and then
# if the string is a permutation of it

# First solution: Check if the string is palindrome-able by scanning to see if there are
# enough duplicate letters and then check permutations
def is_palindrome_permutation(string_1, string_2):
    dictionary_watch = {}

    for char in string_1:
        if dictionary_watch.get(char) == None:
            dictionary_watch[char] = 1
        else:
            dictionary_watch[char] += 1

    even_count = 0
    for key in dictionary_watch:
        if dictionary_watch[key] % 2 == 0:
            even_count += 1
    
    if len(string_1) % 2 == 0:
        return False
    elif even_count == len(string_1) - 1:
        pass
    else:
        return False
    
    for char in string_2:
        if dictionary_watch.get(char) != None:
            dictionary_watch[char] -= 1
        else:
            return False
    
    for key in dictionary_watch:
        if dictionary_watch[key] != 0:
            return False
    
    return True

import time
from random import choice
from string import lowercase
from timeit import default_timer as timer
string_val = "".join(choice(lowercase) for i in range(1000))


start_time = timer()
val_1 = is_palindrome_permutation("Hello", "Hello") # False Case
val_2 = is_palindrome_permutation("Hannah", "Hannah") # True Case
val_3 = is_palindrome_permutation("Hannah", "Haahnn") # True Case
val_4 = is_palindrome_permutation("rfv bgt", "tgb vfr") # False Case
val_5 = is_palindrome_permutation(string_val, string_val) # Long Case
end_time = timer()
print(str.format("is_palindrome_permutation: {} {} {} {} {} {}", val_1, val_2, val_3, val_4, val_5, end_time - start_time ))