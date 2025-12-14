# dictionary :

# A dictionary is a collection of key-value pairs.
# It is unordered, changeable, and does not allow duplicate keys.
# Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
# Creating a dictionary


# keys()- Returns all the keys in the dictionary.

d = {"name": "Srikamal", "age": 22}
print(d.keys())

# values()- Returns all the values in the dictionary.

print(d.values())

# items()- Returns all key–value pairs as tuples inside a list-like view.

print(d.items())

# get(key)- Returns the value of the key. If key doesn’t exist, returns None.

print(d.get("name"))   # Srikamal
print(d.get("salary")) # None

# update()- Adds new items or updates existing keys.

d.update({"city": "Gudivada", "age": 23})

# pop(key)- Removes the key and returns its value.

d = {"a": 1, "b": 2}
print(d.pop("a"))   # 1

# popitem()- Removes and returns the last inserted key–value pair.

d = {"a": 1, "b": 2}
print(d.popitem())  # ('b', 2)

#setdefault(key, value)-

#If key exists → returns its value
# #If key does NOT exist → adds key with value

d = {"name": "Srikamal"}
d.setdefault("age", 22)
print(d)

# clear()- Removes all items → dictionary becomes empty.

d.clear()

# copy()- Returns a shallow copy of the dictionary.

d1 = {"x": 10}
d2 = d1.copy()