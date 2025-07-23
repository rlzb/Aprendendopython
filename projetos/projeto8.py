# This for loop iterates through the numbers 0 to 6. The if statement
# Uses the modulo operator to test if the "x" variable is divisible by
# 2. if True, the if statement will print the value of "x". Since no
# Incremental value is specified in the range() paraneters, the default
# Increment is +1

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)