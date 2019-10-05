# Find if each character is unique in a string (speed/modular optimized)
def is_unique_speed(str_check):
    char_map = {}
    for char in str_check:
        hchar = hash(char)
        if char_map.get(hchar) == None:
            char_map[hchar] = 1
            continue
        return False
    return True # O(n) | Space O(k) where k is the number of unique characters in str_check

# '' Space optimized
def is_unique_space(str_check):
    for i in range(len(str_check)):
        for x in range(len(str_check) - i):
            if str_check[i] == str_check[x + 1]:
                return False
    return True # O(n^2) | Space O(1)

# See if a string is a permutation of another string (speed/modular optimized)
def are_permutations_speed(str_check1, str_check2):
    char_map = {}
    for char in str_check1:
        hchar = hash(char)
        if char_map.get(hchar) == None:
            char_map[hchar] = 1
            continue
        char_map[hchar] += 1

    for char in str_check2:
        hchar = hash(char)
        if char_map.get(hchar) == None or char_map.get(hchar) == 0:
            return False
        char_map[hchar] -= 1

    return True # O(n + p) where p is the size of str_check2 | Space O(k) where k is the number of unique characters in str_check2

# See if a string is a permutation of another string (space optimized)
def are_permutations_space(str_check1, str_check2):
    for iter_char in str_check1: # Get char
        count = 0
        for count_char in str_check1: # look for occurences
            if iter_char == count_char:
                count += 1
            for iter_char2 in str_check2:
                if count == 0 and iter_char == iter_char2:
                    return False
                if iter_char == iter_char2:
                    count -= 1
            if count != 0:
                return False
    
    return True # O(n^3) | Space O(1)

# Replace all the occurences of a space within a string with %20 (speed and modular optimized)/ not done for space b/c python 
def space_replace_speed(str_check):
    str_list = list(str_check)
    for x in range(len(str_list)):
        if str_list[x] == " ":
            str_list[x] = "%20"
    return "".join(str_list) # O(n) | Space O(n)
    
# Find if 2 strings are palindrome permutations of each other (speed and modular optimized)
def check_permutation_palindrome_speed(str_check1, str_check2):
    if not is_palindrome(str_check1) or not is_palindrome(str_check2):
        return False
    
    return are_permutations_speed(str_check1, str_check2) # O(n) | Space O(k) where k is the number of unique characters in str_check1

def is_palindrome(str_check):
    char_map = {}
    for char in str_check:
        hchar = hash(char)
        if char_map.get(hchar) == None:
            char_map[hchar] = 1
            continue
        char_map[hchar] += 1
    
    uneven_val = False
    for key in char_map:
        if char_map[key] % 2 != 0 and uneven_val == True:
            return False
        elif char_map[key] % 2 != 0 and uneven_val == False:
            uneven_val = True
    return True

# Check if 2 strings are 1 or 0 edits away (speed and modular optimized)
def is_one_away(str_check1, str_check2):
    if len(str_check1) == len(str_check2):
        return check_replace_or_none(str_check1, str_check2)
    elif len(str_check1) == len(str_check2) + 1:
        return check_insert_or_none(str_check1, str_check2)
    elif len(str_check1) + 1 == len(str_check2):
        return check_insert_or_none(str_check1, str_check1)
    
    return False # O(n) | Space O(1)

def check_insert_or_none(str_check1, str_check2):
    other_index = 0
    for x in range(len(str_check1)):
        if other_index >= x + 2:
            return False
        elif str_check1[x] != str_check2[other_index]:
            other_index += 1
            continue
        other_index += 1

    return True

def check_replace_or_none(str_check1, str_check2):
    one_off = False
    for x in range(len(str_check1)):
        if str_check1[x] != str_check2[x] and one_off:
            return False
        elif str_check1[x] != str_check2[x] and not one_off:
            one_off = True
    return True

# Compress a string with this pattern => aaabbccaa -> a3b2c2a2
def compress_string_count(str_cmp):
    cmp_string_list = []
    current_char = ""
    count = 0
    for x in range(len(str_cmp)):
        if current_char == "":
            current_char = str_cmp[x]
            x -= 1
            continue
        elif current_char != str_cmp[x]:
            cmp_string_list.append(str.format("{}{}", current_char, count))
            current_char = str_cmp[x]
            x -= 1
        count += 1

    return "".join(cmp_string_list) # O(n) | Space O(n)
