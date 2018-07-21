# One away edits can be grouped into 3 categories: add a character, remove a character and 
# replace a character. Write a method that checks if a string is one or zero edits 
# away from another

# First Solution: Go through the first string and check if the second string has all the
# characters as the first except 1 as with one awaya there should be an exact match on
# all other elements
def is_one_away(string_1, string_2):
    unique_items = {}

    for char in string_1:
        if unique_items.get(char) == None:
            unique_items[char] = 1
        else:
            unique_items[char] += 1