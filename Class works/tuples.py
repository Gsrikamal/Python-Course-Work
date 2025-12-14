# basic methods for tuples: 

# tuples are immutable, so methods that modify the tuple will return a new tuple    

t=(10,20,30,20,40,50,20)
print(t.count(20))        # count() - returns the number of occurrences of a specified value
print(t.index(40))       # index() - returns the index of the first occurrence of   a specified value 

# extra useful operations (not methods) for tuples:
  
print(len(t))           # length()- returns the length of the tuple
print(min(t))           # min() - returns the smallest item in the tuple
print(max(t))           # max() - returns the largest item in the tuple 
 
t1=(10,20,30)
t2=(40,50,60)
print(t1 + t2)        # concatenation - combines two tuples 
print(t1 * 3)         # repetition - repeats the tuple multiple times
print(20 in t)        # membership - checks if an item exists in the tuple
print(t1[2])           # indexing - accesses an item at a specific index
print(t1[1:5])         # slicing - accesses a range of items in the tuple
print(sorted(t1))      # sorted() - returns a sorted list of the tuple's items


