# Create the method isSubstring in which it checks if one word is the substring of the other.
# Now write a method to see if one string is the rotation of the other (a rotation meaning
# "banana" ==> "nabana", which is a rotation to the right by 2) by using only one method
# call to isSubstring

# First Solution: Look into shifting each character to the back until there is either a match
# found or the loop ends, found duplicate answer in duplicating the string, and checking if 
# substring
def is_rotation(string_1, string_2):
    
    if len(string_1) == len(string_2):
        new_string = string_1 + string_1
        return isSubstring(new_string, string_2)
    return False

# First Solution: Failure to come up with a clean method, realized that python can handle it with a simple in call
def isSubstring(string_1, string_2):
    if string_2 in string_1:
        return True

    return False



print (isSubstring("Hello","ello"))
print (isSubstring("Hello","He"))
print (isSubstring("Hello","Blah"))
print (isSubstring("Hello","oH"))
print("-----")
print (is_rotation("Hello","oH"))
print (is_rotation("Hello","oHell"))