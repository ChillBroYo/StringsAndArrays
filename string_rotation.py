# Create the method isSubstring in which it checks if one word is the substring of the other.
# Now write a method to see if one string is the rotation of the other (a rotation meaning
# "banana" ==> "nabana", which is a rotation to the right by 2) by using only one method
# call to isSubstring

# First Solution: since there must be an exact match of the pattern, start at the first letter
# in the first set, find it in the second set and see if the following pattern matches, if not,
# move on to the next occurence of the character, do this until either the pattern matches or 
# if there are no more occurences to which, return false
def is_rotated_string(string_1, string_2):
    counter = 0
    for str_1_index in range(len(string_1)):
        if string_1[str_1_index] in string_2:
            start_index = string_2.find(string_1[str_1_index])
            for x in range(len(string_1)):
                if start_index + x > len(string_2) and string_1[x] == string_2[(start_index + x) - len(string_2)]:
                    counter += 1
                else:
                    counter = 0
                    break

                if string_1[x] == string_2[start_index + x]:
                    counter += 1
                else:
                    counter = 0
                    break
            print(counter)
            if counter == len(string_1):
                return True
        else:
            return False

    return False

print(is_rotated_string("Hello", "oHell"))