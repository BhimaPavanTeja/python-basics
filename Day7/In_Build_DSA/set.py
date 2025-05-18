# Set Functions (Mutable, Unordered, No Duplicates)
#Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print("add:", my_set)  

my_set.remove(6)
print("remove:", my_set)  

my_set.discard(6)  
print("discard:", my_set)  

popped_item = my_set.pop()
print("pop:", my_set, "popped item:", popped_item) 

my_set.clear()
print("clear:", my_set)

my_set = {1, 2, 3}
other_set = {3, 4, 5}
union_set = my_set.union(other_set)
print("union:", union_set) 

intersection_set = my_set.intersection(other_set)
print("intersection:", intersection_set) 

difference_set = my_set.difference(other_set)
print("difference:", difference_set) 

sym_diff_set = my_set.symmetric_difference(other_set)
print("symmetric_difference:", sym_diff_set) 

print("issubset:", my_set.issubset({1, 2, 3, 4}))

print("issuperset:", my_set.issuperset({1, 2}))


print("isdisjoint:", my_set.isdisjoint({4, 5}))

set_copy = my_set.copy()
print("copy:", set_copy) 