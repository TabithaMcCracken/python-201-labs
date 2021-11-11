# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.


# I'm struggling to come up with an example for this one so this is what I did
# Take in a number between 1-50 and either double it until its 25 or more and 
# then add 1 until the number is 50

val = int(input("Please enter a number between 1 and 50: "))
print(val)

def evaluate_val(num):
    if num == 50:
        print("You now have 50!!!")
    elif num <= 25:
        double_num(num)
    elif num>25 and num<50:
        add_one(num)

def double_num(num):
    num = num * 2
    print(f"We doubled your number and its now: {num}")
    if num > 25 and num < 50:
        add_one(num)
    else:
        double_num(num)

def add_one(num):
    num += 1
    print(f"We added 1 to your number and now it's: {num}")
    if num < 50:
        add_one(num)
    else:
        evaluate_val(num)

evaluate_val(val)