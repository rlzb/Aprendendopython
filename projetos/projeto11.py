# This function uses a set of nested for loops with the range() function
# To create the matrix of numbers. T upper range value in the range()
# function should be included in the matrix. The matrix should consist
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):
    
    
    # It is an optional code styple to assign the long variable names in the 
    # function parameters to shorter variables names.
    n1 = initial_number
    n2 = end_of_first_row +1
    
    
    # The first for loop will create the rows.
    for column in range(n1, n2):
        
        # The nested for loop will create the rows.
        for row in range(n1, n2):
            # To make the matrix of numbers easier to read, Include a space
            # between each number in the rows until the loop reaches the
            # end of the row. You can Override the default behavior of the
            # print() function (witch inserts a new line character afret 
            # the print command runs) by using the "end="" parameter
            # Inside the print() function.
            print(column * row, end=" ")
            
        # The row ends when the upper range value is encountred within the
        # Nested for loop. The outer (column) for loop should insert a new line 
        # To create the next row. Use the print() function new line default
        # Behavior with an empty print() function:
        print()
        
        
# Call the function with 2 integer parameters.
matrix(1,4)
# Should print;
# 1 2 3 4
# 2 4 6 9
# 3 6 9 12
# 4 8 12 16
for outer_loop in range(10):
    
    
    for inner_loop in range(outer_loop):
        print(inner_loop)
        
#####################################################
for n in range(11, -2):
    if n % 2 != 0:                          # Test
        print(n, end=" ")
        
######################################################
starting_number = 18

# THe while loop will continue to loop until it reaches 0.
while starting_number >= -0:
    
    # To make the sequence of numbers easier to real, include a space
    # Between each number in the sequence. You can override the default 
    # the print() function.  The syntax for adding a space is: end=" "
    print(starting_number, end=" ")
    
    # Decrement the "starting number" variable by -3.
    starting_number -= 3
    # Should print 18 15 12 9 6 3 0