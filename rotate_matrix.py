# Rotate a NxN matrix 90 degrees where each pixel is 4 bytes. Bonus do this in place without
# any other data usage

# Solution: Do a transposition to rotate axis of all digits, then invert the position of
# the columns for clockwise rotation, invert position of rows for counter clock
def rotate_matrix_90(matrix_val, counter_clock_rotation=False):
    # a b c d       m i e a
    # e f g h  ---> n j f b
    # i j k l       o k g c
    # m n o p       p l h d
    transpose(matrix_val)

    # Shift columns for counter clockwise 90 degrees rotation
    # swap items in first half for items in second half
    if not counter_clock_rotation:
        for y in range(len(matrix_val)):
            for x in range(len(matrix_val[y])//2):
                temp_val = matrix_val[y][x]
                matrix_val[y][x] = matrix_val[y][len(matrix_val[x]) - 1 - x]
                matrix_val[y][len(matrix_val[x]) - 1 - x] = temp_val
    else:
        for y in range(len(matrix_val)//2):
            for x in range(len(matrix_val[y])):
                temp_val = matrix_val[y][x]
                matrix_val[y][x] = matrix_val[len(matrix_val[y]) - 1 - y][x]
                matrix_val[len(matrix_val[y]) - 1 - y][x] = temp_val

        
    return matrix_val

# Transpose an NxN matrix
def transpose(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x < y:
                y = x
            temp_val = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp_val
    



val = [ ["a","b","c","d"],
        ["e","f","g","h"],
        ["i","j","k","l"],
        ["m","n","o","p"]]

print(val)
print(rotate_matrix_90(val))
print(rotate_matrix_90(val))
print(rotate_matrix_90(val))
print(rotate_matrix_90(val))

val = [ ["a","b","c","d"],
        ["e","f","g","h"],
        ["i","j","k","l"],
        ["m","n","o","p"]]

print(rotate_matrix_90(val, True))

print("-----")


val = [ ["a","b","c","d","e"],
        ["f","g","h","i","j"],
        ["k","l","m","n","o"],
        ["p","q","r","s","t"],
        ["u","v","w","x","y"]]

print(val)
print(rotate_matrix_90(val))

val = [ ["a","b","c","d","e"],
        ["f","g","h","i","j"],
        ["k","l","m","n","o"],
        ["p","q","r","s","t"],
        ["u","v","w","x","y"]]

print(rotate_matrix_90(val, True))