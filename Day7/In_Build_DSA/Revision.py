# Lists
# List Operations
lst1 = [1, 2]
lst2 = [3, 4]
print(lst1 + lst2)  # Concatenation: [1, 2, 3, 4]
print(lst1 * 2)     # Repetition: [1, 2, 1, 2]

# List Slices
lst = [1, 2, 3, 4, 5]
print(lst[1:4])     # [2, 3, 4]

# List Methods
lst = [1, 3, 2]
lst.append(4)       # Append 4 to the list: [1, 3, 2, 4]
lst.sort()          # Sort the list: [1, 2, 3, 4]

# List Loop
for item in [1, 2, 3]:
    print(item)

# Mutability
lst = [1, 2, 3]
lst[0] = 10         # List after modification: [10, 2, 3]

# Aliasing
lst1 = [1, 2]
lst2 = lst1
lst2[0] = 10
print(lst1)         # [10, 2]

# Cloning Lists
lst1 = [1, 2]
lst2 = lst1[:]
lst2[0] = 10
print(lst1)         # [1, 2]

# List Parameters
def modify(lst):
    lst.append(100)

lst = [1, 2, 3]
modify(lst)
print(lst)          # [1, 2, 3, 100]

# List Comprehension
lst = [x**2 for x in range(5)]
print(lst)          # [0, 1, 4, 9, 16]

# Tuples
# Tuple Assignment
tup = (1, 2, 3)
a, b, c = tup
print(a, b, c)      # 1 2 3

# Tuple as Return Value
def get_values():
    return 1, 2, 3

a, b, c = get_values()
print(a, b, c)      # 1 2 3

# Tuple Comprehension
tup = tuple(x**2 for x in range(5))
print(tup)          # (0, 1, 4, 9, 16)

# Dictionaries
# Operations and Methods
d = {'a': 1, 'b': 2}
d['c'] = 3           # Add a new key-value pair
print(d['a'])        # Access value: 1

# Dictionary Methods
print(d.get('a'))    # Get value by key: 1
print(d.keys())      # Get all keys: dict_keys(['a', 'b', 'c'])

# Dictionary Comprehension
d = {x: x**2 for x in range(5)}
print(d)            # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
