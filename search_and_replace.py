# Find specified character in string and replace with supplied one in place
# Strategy: Create new string with properly filled values after splitting inital string
# O(n) => linear | Mem Usage: O(n) => linear

def search_and_r(s_string, char_to_r, char_to_rw):
    f_string = []
    for char in s_string:
        if char == char_to_r:
            f_string.append(char_to_rw)
        else:
            f_string.append(char)

    return ''.join(f_string)


# Find any sized 'word' in set and replace with supplied 'word'
# Strategy: Loop over entire string, whenever a match seems to be found, stop and check next characters, if success append new 'word' and move iterator, if not resume iterative loop
# Worst case goes over the whole set twice O(2n) => O(n) | Mem Usage: O(n) => linear
def search_and_r_word(s_string, word_to_r, word_to_rw):
    string_list = []
    i = 0
    while i < len(s_string):
        if s_string[i] == word_to_r[0]:
            match = True
            for x in range(len(word_to_r)):
                if len(s_string[i:]) < len(word_to_r) or s_string[i + x] != word_to_r[x]:
                    match = False
            if match == True:
                string_list.append(word_to_rw)
                i += len(word_to_r)
                continue

        string_list.append(s_string[i])
        i += 1
    
    return ''.join(string_list)


if __name__ == "__main__":
    import time
    from random import choice
    import string
    from timeit import default_timer as timer

    print(search_and_r_word("Hello World", "Wo", "%20"))
    print(search_and_r_word("Hello World", "l d", "%20"))
    print(search_and_r_word("Hello World", "l", "%20"))
    print(search_and_r_word("Hello World", "World", "%20"))