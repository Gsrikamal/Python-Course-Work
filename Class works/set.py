# SET METHODS (with examples)

# add()----------------Adds one element

s = {1, 2}
s.add(3)
print(s)

# update()---------Adds multiple elements

s = {1, 2}
s.update([3, 4, 5])
print(s)

# remove()-----------Removes element (❌ error if not found)

s = {1, 2, 3}
s.remove(2)

# discard()-----------Removes element (✔ no error if not found)

s.discard(5)

# pop()------------------Removes a random element

s.pop()

# clear()----------------Removes all elements

s.clear()

# copy()---------------------- Returns a shallow copy

s2 = s.copy()

# SET OPERATIONS (Important ⭐)


# Union (| or union())-----------------All elements from both sets

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))

# Intersection (& or intersection())--------  Common elements

print(a & b)
print(a.intersection(b))

# Difference (- or difference())-         Elements in first set only

print(a - b)
print(a.difference(b))

# Symmetric Difference (^ or symmetric_difference())-   Elements NOT common

print(a ^ b)
print(a.symmetric_difference(b))

# SET RELATIONAL METHODS

# issubset()- All elements of first set in second set
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# issuperset()- All elements of first set in second set
print(b.issuperset(a))

# isdisjoint()- No common elements

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))