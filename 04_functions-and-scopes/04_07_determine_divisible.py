# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


def four_or_seven (user_num):
    """Determines whether num is divisible by 4 or 7"""

    if user_num % 7 == 0 or user_num % 4 == 0:
        flag = True
    else:
        flag = False
    return flag

def four_and_seven(user_num):
    """Determines whether num is divisible by 4 and 7"""

    if user_num % 7 == 0 and user_num % 4 == 0:
        flag = True
    else:
        flag = False
    return flag

flag = False
min = 1
max = 1000000000

while flag == False:
    user_num = int(input("Please enter a number between 1 and 1,000,000,000:"))
    if user_num >= min and user_num <= max:
            flag = True

or_response = four_or_seven(user_num)
if or_response == True:
    print("Your number is divisible by either 7 or 4.")
else:
    print("Your number is not divisibale by 7 or 4.")

and_response = four_and_seven(user_num)
if and_response == True:
    print("Your number is divisiable by 7 and 4.")
else:
    print("Your number is not divisble by both 7 and 4.")