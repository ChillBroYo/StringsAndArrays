# Determine if two strings are permutations of each other

#-- First Solution: Check if the letters in one string exist in the other string in a loop
#-- Run Complexity: O(N * K) || In the worst case, loops over the original set once per the
# second set's characters (where n represents the len(string_1) and k represents len(string_2))
#-- Space Complexity: O(1) || All memory used is in place and does not use any additional storage
def is_permutation(string_1, string_2):
    permutation = True

    # Size check
    if len(string_1) != len(string_2):
        return False

    # For each character in string_1, see if it exists in string_2
    for char in string_1:
        exists = False
        for x in range(len(string_2)):

            # If character exists in string_2, remove item from string_2 and break out
            if char == string_2[x]:
                exists = True
                string_2 = string_2.replace(string_2[x], "", 1)
                break
        # If any character did not appear, return false
        if exists == False:
            permutation = False
            break
    
    return permutation


#-- Improved Speed Solution: Store all the items in a hashtable using the string as a key attached
# to a value counting the number of appearances. Then see which characters appear in string_2
#-- Runtime Complexity: O(2N + K) => O(N + K) || Loops over the first set twice and the second 
# set once where n is the len(string_1) and k is the len(string_2)
#-- Space Complexity: O(N) || Stores a hash table of values the same size as the first string
def is_permutation_faster(string_1, string_2):
    hash_table = {}

    # Store count of each element appearing in the initial set
    for char in string_1:
        if hash_table.get(char) == None:
            hash_table[char] = 1
        else:
            hash_table[char] += 1

    # Remove occurences of second string from first
    for char in string_2:
        if hash_table.get(char) == None or hash_table.get(char) == 0:
            return False
        else:
            hash_table[char] -= 1

    # See if any occurences from first set remain
    for key in hash_table:
        if hash_table[key] != 0:
            return False

    return True

import time
from random import choice
from string import lowercase
from timeit import default_timer as timer
string_val = "".join(choice(lowercase) for i in range(10000))


start_time = timer()
val_1 = is_permutation("Hello", "olleH") # True Case
val_2 = is_permutation("aHello", "Hello") # False Case
val_3 = is_permutation("Hello", "olleHa") # False Case
val_4 = is_permutation("rfv bgt", "tgb vfr") # True Case
val_5 = is_permutation(string_val, string_val) # Long Case
end_time = timer()
print(str.format("isPermutation: {} {} {} {} {} {}", val_1, val_2, val_3, val_4, val_5, end_time - start_time ))

start_time = timer()
val_1 = is_permutation_faster("Hello", "olleH") # True Case
val_2 = is_permutation_faster("aHello", "Hello") # False Case
val_3 = is_permutation_faster("Hello", "olleHa") # False Case
val_4 = is_permutation_faster("rfv bgt", "tgb vfr") # True Case
val_5 = is_permutation_faster(string_val, string_val) # Long Case
end_time = timer()
print(str.format("isPermutation: {} {} {} {} {} {}", val_1, val_2, val_3, val_4, val_5, end_time - start_time ))