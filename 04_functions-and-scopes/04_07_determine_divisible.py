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

    if user_num % 7 or user_num % 4 == True:
        flag = True
    else:
        flag = False
    return flag

# answer = four_or_seven(42)

flag = False
min = 1
max = 1000000000

while flag == False:
    user_num = int(input("Please enter a number between 1 and 1,000,000,000:"))
    if user_num >= min and user_num <= max:
            flag = True

boolean_response = four_or_seven(user_num)
print(boolean_response)