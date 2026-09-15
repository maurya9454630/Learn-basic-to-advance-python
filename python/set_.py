# set is the collection of the unorderd iteams.
# each elements in the set must be unique & immutable.

set1 = {1, 2, 4, 3, 2, "ram", "sayam"}
print(set1)

set2 = set() #empty set
set2.add(1)
set2.add(2) # add new value
print(set2)
set2.remove(2) # remove a value
print(set2)
set2.add((4,6,7,4,8,32,0,))
print(set2)
print(set2.pop()) # random value remove
print(set2.clear()) # all clear data 
print(len(set2))

collection1 = {1, 2, 4}
collection2 = {3, 4, 5}
print(collection1.union(collection2)) # combines both set values & return new

print(collection1.intersection(collection2)) # combians common values & return value.