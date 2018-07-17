# Replace all the spaces in a string with %20, ensure that the operation is done in place and without any additional data structures. There must be a true length of the string that must be followed:
# input "hello  there " length = 11 => "hello%20there"

#-- First Solution: Pass through entire character array, aggregrating all space chunks into
# one %20 and stripping beginning and ending
#-- Runtime Complexity: O(N) || Runs through the string exactly once
#-- Space Complexity: O(N) || Unable to meet condition of in place due to python string immutability,
# compesated by not using any additional space besides initial conversion into list from string and
# rejoin value, could be seen as using space needed for the original set
def urlify(string_to_convert):

    # Convert to list and remove trailing and beginning spaces
    string_to_convert = list(string_to_convert.strip())

    # Iterate through string, removing spaces that are not directly connected to a non-space
    # and converting spaces connected to non-spaces with %20
    for x in range(len(string_to_convert) - 1):
        if string_to_convert[x] == " " and string_to_convert[x + 1] != " ":
            string_to_convert[x] = "%20"
        elif string_to_convert[x] == " " and string_to_convert[x + 1] == " ":
            del string_to_convert[x]

    return ''.join(string_to_convert)


import time
from random import choice
from string import lowercase
from timeit import default_timer as timer
string_val = "".join(choice(lowercase) for i in range(1000))


start_time = timer()
val_1 = urlify("Hello").count("%20") == 0 # None Case
val_2 = urlify(" That isn't possible ").count("%20") == 2 # 2 Case
val_3 = urlify("l That isn't possible l").count("%20") == 4 # 4 Case
val_4 = urlify("Safe w ord").count("%20") == 2 # Weird 2 Case
val_5 = urlify(string_val).count("%20") == 0 # Long 0 Case
end_time = timer()
print(str.format("urlify: {} || {} || {} || {} || {}", val_1, val_2, val_3, val_4, end_time - start_time ))