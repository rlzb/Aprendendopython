# Variables - Know how to correctly initialize or increment a variable.
# You also need to recognize coding errors caused by failure to initialize or increment properly.

# Infinite loops - Learn to recognize infinite loops and use common solutions to avoid them.
# For example, check loop conditions, ranges, iterators, control statements, etc.,
# to make sure at least one control is in place to prevent an infinite loop.

# Iterators - Understand the various ways to iterate over a variable
# (e.g., using assignment operators, using the third parameter of the range() function).
# You must also analyze where the iteration should occur.
# A poorly positioned iterator can produce the wrong result or create an infinite loop.

# Control statements - Know how and when to use the break and continue statements to avoid infinite loops.

# Common functions

# Parameters of the range() function - Know the roles of the three possible parameters in range(x, y, z):

# x: Start of the range (inclusive)
# y: End of the range (exclusive index)
#    To include the end index in the range, use the expression y+1.
#    The end of the range must be included in the parameters of range().

# z: Increment value

# Example 1: range(4, 12+1, 2)
# This example creates a range starting at 4 and ending at 12.
# Without the +1, the range would end at 11.
# The third parameter increments the iteration by 2 instead of the default 1.
# This expression produces the values: 4, 6, 8, 10, 12

# Example 2: range(10, 2-1, -2)
# This example creates a range starting at 10 and ending at 2-1, with a decrement value of -2.
# When counting down, to include the end index value, use -1 (end of range minus 1).
# This range produces the sequence: 10, 8, 6, 4, 2

# Default behavior of the print() function - Know that the default behavior of print() is to add a newline character after execution.

# To override the newline and replace it with a space, add end=" " as the last parameter in print().
# This allows the next output to appear on the same line, separated by a space.
# You can use this technique when a print() function is part of a for or while loop.
# Syntax example: print(x + 1, end=" ")

# Coding Skills

# Skill 1: Using for loops with the range() function
# Use a for loop with the range() function including the end of the range by using y+1.


# This function will accept an integer variable "end" and count by 10 
# from 0 to the "end" value
def count_by_10(end):
    # initialize the "count" variable as strikg.
    count = ""
    
    # The rang function parameters instruct Python to start the count
    # at0 and stop at the variable given as the upper end of the range.
    # Since the value of the high end of a range is excluded by default, 
    # you can make Python includ the "end" value by adding +1 to it
    # The third parameter tells Python to increment the count by 10
    for number in range(0, end+1, 10):
        # Although the variable "count" will hold a count of integers,
        # This  example will be converted to string using "Str"(number)"
        # in order to display the incremental count from 0 to the "end"
        # Number
        count += str(number) + " "
        # The .strip() method will trim the final space " " from the end of
        # The string "count"
    return count.strip()
    # Call the function with 1 integer parameter
print(count_by_10(100)) # should print 0 10 20 30 40 50 60 70 80 90 100