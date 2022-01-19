# Using the given variables `base` and `digits`, write a dictionary comprehension
# that maps each integer between `0` and `999` to the list of three digits 
# that represents that integer in base 10. That is, the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
# 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
# 999: [9, 9, 9]}
#
# Your expression should work for any base. For example, 
# if you instead assign 2 to base and assign {0,1} to digits, 
# the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],
# ..., 7: [1, 1, 1]}

base = 10
digits = set(range(base))

# First Attempt using base 10

# dict_ = { num: [int(num/100), int(num/10)%10, num%10] for num in range (0,1000)}
# print(dict_)

# Second Attempt- I had to google this to come up with the x,y,z approach. Still not 
# sure how the comprehension knows what the x,y,and z represent
dict_2 = {(x*base**2 + y*base**1 + z*base**0): [x,y,z] for x in digits for y in digits for z in digits}
print(dict_2)
