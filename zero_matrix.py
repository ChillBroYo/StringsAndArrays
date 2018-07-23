# Write an algorithm such that if an element in an MxN matrix is 0, its entire column and 
# row are set to 0

# First solution: create an dictionary of values that will act as a memory for which 
# values need to be zero'd out
def zero_matrix(matrix_val):
    y_check = {}
    x_check = {}

    # Find 0 values
    for y in range(len(matrix_val)):
        for x in range(len(matrix_val[y])):
            if matrix_val[y][x] == 0:
                y_check[y] = 1
                x_check[x] = 1
    
    # Set 0 values
    for y in range(len(matrix_val)):
        for x in range(len(matrix_val[y])):
            if y_check.get(y) == 1 or x_check.get(x) == 1:
                matrix_val[y][x] = 0

    return matrix_val

val_1 = [[1,2,3],
         [4,0,6],
         [7,8,9]]
val_2 = [[1,0],
         [4,5],
         [7,8]]
val_3 = [[1,0,3],
         [4,5,6]]

print(zero_matrix(val_1))
print(zero_matrix(val_2))
print(zero_matrix(val_3))
    