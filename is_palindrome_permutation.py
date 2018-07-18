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
    from string import lowercase
    from timeit import default_timer as timer
    string_val = "".join(choice(lowercase) for i in range(1000))


    start_time = timer()
    val_1 = is_palindrome_permutation("Hello", "Hello")  # False Case
    val_2 = is_palindrome_permutation("HannaH", "HannaH")  # True Case
    val_3 = is_palindrome_permutation("HannaH", "HaaHnn")  # True Case
    val_4 = is_palindrome_permutation("Hannah", "Haahnn")  # False Case
    val_5 = is_palindrome_permutation("rfv bgt", "tgb vfr")  # False Case
    val_6 = is_palindrome_permutation(string_val + string_val, string_val + string_val)  # Long True Case
    end_time = timer()
    print(str.format("is_palindrome_permutation: {} {} {} {} {} {} {}", val_1, val_2, val_3, val_4, val_5,
                    val_6, end_time - start_time))
