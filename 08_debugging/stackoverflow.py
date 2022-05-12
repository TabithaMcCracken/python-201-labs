'''
I want the output to be a==[1], b==[3], but it looks like the update of i does 
not change the elements a or b. In C++, I'd use a pointer but I can't seem to 
find the corresponding concept in Python.
'''

a = [1,2]
b = [2,3]

l = [a,b]

# for i in l:
#     i = [elem for elem in l if elem != 2]
# print (l)


for i in l:
    i.remove(2)

print (l)