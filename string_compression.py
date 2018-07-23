# Implement a method to perform basic string compression on duplicate strings:
# aaaabbbbcccdddd => a4b4c3d4. However, if the compressed string would not be
# smaller than the original string, the function should return the original string. It 
# can be assumed that the string in this case will only be composed of uppercase and 
# lowercase letters.

# First solution: Go over the string once, and count duplicate letters, placing the counts in the new string
def compress_string(string_to_compress, return_compressed_value = False):
    compressed_string = ""
    counter = 1
    character_on = ""
    prev_character = ""
    for char in string_to_compress:
        if char != prev_character and prev_character != "":
            compressed_string += str.format("{}{}", character_on, counter)
            character_on = char
            counter = 1
        elif prev_character == "":
            character_on = char
            counter = 1
        elif char == prev_character:
            counter += 1
        
        prev_character = char
    
    compressed_string += str.format("{}{}", character_on, counter)
    if len(compressed_string) < len(string_to_compress) or return_compressed_value:
        return compressed_string
    
    return string_to_compress

if __name__ == "__main__":
    import time
    from random import choice
    import string
    from timeit import default_timer as timer
    string_val = "".join(choice(string.ascii_lowercase) for i in range(1000))


    start_time = timer()
    val_1 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string("Hello", True), compress_string("Hello"), "Hello")
    val_2 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string(" That isn't possible ", True), compress_string(" That isn't possible "), " That isn't possible ")
    val_3 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string("aaabbbccc", True), compress_string("aaabbbccc"), "aaabbbccc")
    val_4 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string("abc", True), compress_string("abc"), "abc")
    val_5 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string("abcdefff", True), compress_string("abcdefff"), "abcdefff")
    val_6 = str.format("Compressed: {} || Chosen: {} || Input Value: {}",
        compress_string("There once was a man who wore a hat.", True),
            compress_string("There once was a man who wore a hat."), "There once was a man who wore a hat.")
        
    end_time = timer()
    print(val_1)
    print(val_2)
    print(val_3)
    print(val_4)
    print(val_5)
    print(val_6)