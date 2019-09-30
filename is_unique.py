# Implement an algorithm to determine if a string has all unique characters.
# Bonus: Do not use additional data structures

# -- First solution: Use a single list and check entire list each time a new character is added
# -- Run Complexity: O(N^2) || In the worst case, the code needs to check each item n times, to ensure
# each item does not match with any other case
# -- Space Complexity: O(N) || Uses a list of values the same size of the initial set to ensure
# end set is unique
def is_unique(check_string):
    storage_list = []
    for char in check_string:
        for previous_item in storage_list:
            if previous_item == char:
                return False
        storage_list.append(char)

    # If we've checked all the characters and none of them have been repeated, string is unique
    return True


# Determine if a string has all unique characters
# Strategy: Have a map, walkthrough each item and store/check against the map for each character, when a duplicate value is found
# return false else return true
def is_unique_simple(str_check):
    map_store = {}

    for char in str_check:
        hchar = hash(char)
        if map_store.get(hchar) == None:
            map_store[hchar] = 1
        else:
            return False

    return True

# -- Improved speed solution: Places each character into a hash map, knowing if theres a duplicate when an
# identical has value has been generated
# -- Run Complexity: O(n) || In the worst case, the code checks each character in the string exactly
# once
# -- Space Complexity: N || Uses a hashtable of elements the size of the original string
def is_unique_faster(check_string):
    hash_storage = {}
    unique = True
    for char in check_string:
        h_val = hash(char)

        # If the hash key has no value, assign one, if it already does the set is not unique
        if hash_storage.get(h_val) == None:
            hash_storage[h_val] = 1
        else:
            unique = False
            break

    return unique


if __name__ == "__main__":
    import time
    from random import choice
    import string
    from timeit import default_timer as timer

    rnd_words = []
    for i in range(1000):
        rnd_words.append("".join(choice(string.ascii_lowercase) for i in range(1000)))


    start_time = timer()
    val_1 = is_unique("Hello")  # False Case
    val_2 = is_unique("That isn't possible")  # False Case
    val_3 = is_unique("Safe word")  # Success Case
    for i in rnd_words:
        is_unique(i)
    end_time = timer()
    print(str.format("is_unique:        {} {} {} {}", val_1,val_2, val_3, end_time - start_time))

    start_time = timer()
    val_5 = is_unique("Hello")  # False Case
    val_6 = is_unique("That isn't possible")  # False Case
    val_7 = is_unique("Safe word")  # Success Case
    for i in rnd_words:
        is_unique_simple(i)
    end_time = timer()
    print(str.format("is_unique2:       {} {} {} {}", val_5, val_6, val_7, end_time - start_time))

    start_time = timer()
    val_1 = is_unique_faster("Hello")  # False Case
    val_2 = is_unique_faster("That isn't possible")  # False Case
    val_3 = is_unique_faster("Safe word")  # Success Case
    for i in rnd_words:
        is_unique_faster(i)
    end_time = timer()
    print(str.format("is_unique_faster: {} {} {} {}", val_1, val_2, val_3, end_time - start_time))
