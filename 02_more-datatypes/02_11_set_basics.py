# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets
# - Create a union of both sets

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

# Intersection 
u = {}
u = s.intersection(t)
print("This is the intersection of s and t:")
print(u)

# Union
v = {}
v = s.union(t)
print("This is the union of s and t:")
print(v)