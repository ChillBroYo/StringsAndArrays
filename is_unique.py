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
    from string import lowercase
    from timeit import default_timer as timer
    string_val = "".join(choice(lowercase) for i in range(1000000))


    start_time = timer()
    val_1 = is_unique("Hello")  # False Case
    val_2 = is_unique("That isn't possible")  # False Case
    val_3 = is_unique("Safe word")  # Success Case
    val_4 = is_unique(string_val)  # Long Case
    end_time = timer()
    print(str.format("isUnique: {} {} {} {} {}", val_1,
                    val_2, val_3, val_4, end_time - start_time))

    start_time = timer()
    val_1 = is_unique_faster("Hello")  # False Case
    val_2 = is_unique_faster("That isn't possible")  # False Case
    val_3 = is_unique_faster("Safe word")  # Success Case
    val_4 = is_unique_faster(string_val)  # Long Case
    end_time = timer()
    print(str.format("isUniqueFaster: {} {} {} {} {}",
                    val_1, val_2, val_3, val_4, end_time - start_time))
