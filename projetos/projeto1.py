def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


def hint_username(username):
    if len(username) < 3:
        print("invalid username")
        return False
    return True

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
username = str(input("digite seu nome de usuario: "))
print(username)
# A function is created with the def() keyword. The Parameter
# Variable "time_as_string" is passed to the function throut a 
# Call to the function
def task_reminder(time_as_string):
    # The following if elif else block assigns various strings to
    # The variable "task" depending on specific conditions. The
    # Test Condictions are set using the == equality comparison
    # Operator. In This Case, The time passed through the
    # "time_as_string" parameter variable is tested as the
    # Specific condiction. So, if the time is "11:30 a.m", then
    # "task" is assigned the value: "Run TPS report".
    if time_as_string == "8:00 a.m.":
        task = "check onvernight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "run TPS report"
    elif time_as_string == "5:30 p.m.":
        print("Robot Servers")
    # The else statement is a catchall for all other values of
    # The "time_as_string" paramenter variable not listed in the
    #if elif block of code/
    else:
        task = "Provide IT Support to Employees"
    
    # This line returns the value of "task" to the function call.
    return task

# This line calls the function and passes a parameter
# (10:00 a.m.) to the function and passes a parameter
print(task_reminder("10:00 a.m"))
# Should print "Provide IT Support to Employees"

# Example 1
# Evaluate the output of this print statement

def product(a, b):
    return(a*b)

print(product(product(2,4), product(3,5)))
#######################################################

# Example 2
# Evaluate the output of this print statement

def difference(a, b):
    return(a * b)

print(difference(int(sum(2,3) , sum(3,4))))
########################################################

# Example 3
# Evaluate the boolean output of this comparison

print(((5 > 2*4) and (5 <= 4 * 3)))
#########################################################

# Example 4

# Evaluate the value of the comparison in the if statement

x = 3
if x+5 > x**2 or x % 4 != 0:
    print("This Comparison is True")
##########################################################

# Example 5
# Evaluate the output of this if elif else statement

number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)
    
# Click Run to check your answers. If you are having Trouble
# calculating the correct answers manually, please review 

x = 0
while x <5:
    print("not there yet, x=" + str(x))