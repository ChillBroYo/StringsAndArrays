from is_permutation import is_permutation_faster

# Write a function to check if a string is a permutation of a palindrome of another string,
# a palindrome is a string that is the same backwards and forwards: Hannah <==> Hannah.
# A permutation of a the palindrome "Hannah" would be "Hnnaha"

# Problem clairification: Essentially a check on if the string is a palindrome and then
# if the string is a permutation of it

#-- First solution: Check if the string is palindrome-able by scanning to see if there are
# enough duplicate letters and then check permutations
#-- Runtime Complexity: O(N + H + K) || The set runs over the first string (N) once then runs over
# unique character set (H) and then runs over the second string (K) once in the worst case
#-- Space Complexity: O(N) || In the worst case uses a dictionary of size len(string_1)
def is_palindrome_permutation(string_1, string_2):
    dictionary_watch = {}

    # Return False unless its a palindrome, then run permutation check
    if is_palindrome(string_1, string_2, dictionary_watch):
        return is_permutation_faster(string_1, string_2, dictionary_watch)
    else:
        return False

# Determine if a string is a palindrome
# Strategy: Palindriome must have an even amount of characters for all characters except 1 (not necessary), walk through and count instances
# O(n + k) => O(n) | Mem Usage: O(k)
def is_str_palindrome(str_check):
    char_count = {}
    for char in str_check:
        hchar = hash(char)
        if char_count.get(hchar) == None:
            char_count[hchar] = 1
        else:
            char_count[hchar] += 1
    
    one_exception = False
    for char in char_count:
        if char_count[char] % 2 != 0 and one_exception == True:
            return False
        elif char_count[char] % 2 != 0 and one_exception == False:
            one_exception = True

    return True

# Determine if a string is a palindrome of the other
# Strategy: Both strings must have the same characters, walthrough both and count and see if there's a value at the end
# O(2n + k) | Mem Usage O(2n)
def palindrome_of(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    # If its not a palindrome, no use of checking
    if not is_str_palindrome(str_1):
        return False

    lookup_t = {}
    for i in range(len(str_1)):
        hchar1 = hash(str_1[i])
        hchar2 = hash(str_2[i])

        if lookup_t.get(hchar1) == None:
            lookup_t[hchar1] = 1
        else:
            lookup_t[hchar1] += 1

        if  lookup_t.get(hchar2) == None:
            lookup_t[hchar2] = -1
        else:
            lookup_t[hchar2] -= 1
    
    for hashkey in lookup_t:
        if lookup_t[hashkey] != 0:
            return False
        
    return True

# Find if a strings are panindrome permutations of each other
# Strategy: Seeing if a string is a palindrome is a stronger restriction than palindrome, they should have the same characters
def permute_palindrome_of(str_1, str_2):
    return palindrome_of(str_1, str_2)

# Library solution: The necessity of palindromes are duplicate letters in the string,
# for an even number of characters in the string, each character must have an even number
# of occurences, for an odd number of characters, the same rules apply with the exception
# of one character having an odd number of occurences
#-- Runtime Complexity: O(N + H) || Runs through the first string (N) and the unique set
# of characters (H) a maximum of one time
#-- Space Complexity: O(N) || In the worst case, stores a dictionary of size len(string_1)
def is_palindrome(string_1, string_2, dictionary = {}):

    # Load Dictionary
    for char in string_1:
        if dictionary.get(char) == None:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    even_count = 0
    count = 0
    
    # Count even occurences vs occurences
    for key in dictionary:
        count += 1
        if dictionary[key] % 2 == 0:
            even_count += 1

    # Even string check
    if len(string_1) % 2 == 0 and even_count == count:
        return True
    # Odd String check
    elif len(string_1) % 2 == 1 and even_count == count - 1:
        return True
    else:
        return False

if __name__ == "__main__":
    import time
    from random import choice
    import string
    from timeit import default_timer as timer
    string_val = "".join(choice(string.ascii_lowercase) for i in range(1000))


    start_time = timer()
    print(palindrome_of("Hannah", "Hannah"))
    val_1 = is_palindrome_permutation("Hello", "Hello")  # False Case
    val_2 = is_palindrome_permutation("HannaH", "HannaH")  # True Case
    val_3 = is_palindrome_permutation("HannaH", "HaaHnn")  # True Case
    val_4 = is_palindrome_permutation("Hannah", "Haahnn")  # False Case
    val_5 = is_palindrome_permutation("rfv bgt", "tgb vfr")  # False Case
    val_6 = is_palindrome_permutation(string_val + string_val, string_val + string_val)
    val_7 = permute_palindrome_of(string_val + string_val, string_val + string_val)  # Long True Case
    end_time = timer()
    print(str.format("is_palindrome_permutation: {} {} {} {} {} {} {} {}", val_1, val_2, val_3, val_4, val_5,
                    val_6, val_7, end_time - start_time))
