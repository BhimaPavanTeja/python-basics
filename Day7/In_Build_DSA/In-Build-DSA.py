
# LIST EXAMPLES
# 1. Creating a List
animals = ["dog", "cat", "elephant", "lion"]
print(animals)

# 2. Access List Items
print(animals[0])  # Output: dog

# 3. Change List Items
animals[1] = "tiger"
print(animals)

# 4. Add List Items
animals.append("zebra")
print(animals)

# 5. Insert Item at Specific Index
animals.insert(2, "giraffe")
print(animals)

# 6. Remove List Items
animals.remove("lion")
print(animals)

# 7. Pop Last Item
last_animal = animals.pop()
print(last_animal)

# 8. Sort List
animals.sort()
print(animals)

# 9. Reverse List
animals.reverse()
print(animals)

# 10. List Comprehension
animal_lengths = [len(animal) for animal in animals]
print(animal_lengths)

# TUPLE EXAMPLES
# 1. Creating a Tuple
animals_tuple = ("dog", "cat", "elephant", "lion")
print(animals_tuple)

# 2. Access Tuple Items
print(animals_tuple[0])  # Output: dog

# 3. Unpack Tuple
dog, cat, elephant, lion = animals_tuple
print(dog, cat, elephant, lion)

# 4. Convert Tuple to List
animals_list = list(animals_tuple)
print(animals_list)

# 5. Check if Item Exists in Tuple
print("cat" in animals_tuple)  # Output: True

# 6. Tuple Concatenation
more_animals_tuple = animals_tuple + ("zebra", "giraffe")
print(more_animals_tuple)

# 7. Repeat Tuple
repeated_tuple = animals_tuple * 2
print(repeated_tuple)

# SET EXAMPLES
# 1. Creating a Set
animals_set = {"dog", "cat", "elephant", "lion"}
print(animals_set)

# 2. Add Items to Set
animals_set.add("giraffe")
print(animals_set)

# 3. Remove Items from Set
animals_set.remove("lion")
print(animals_set)

# 4. Check if Item Exists in Set
print("cat" in animals_set)  # Output: True

# 5. Set Union
wild_animals = {"tiger", "lion", "leopard"}
all_animals = animals_set.union(wild_animals)
print(all_animals)

# 6. Set Intersection
common_animals = animals_set.intersection(wild_animals)
print(common_animals)

# 7. Set Difference
unique_animals = animals_set.difference(wild_animals)
print(unique_animals)

# DICTIONARY EXAMPLES
# 1. Creating a Dictionary
animals_dict = {"dog": "canine", "cat": "feline", "elephant": "herbivore"}
print(animals_dict)

# 2. Access Dictionary Items
print(animals_dict["dog"])

# 3. Change Dictionary Item
animals_dict["dog"] = "domesticated canine"
print(animals_dict)

# 4. Add Dictionary Item
animals_dict["lion"] = "big cat"
print(animals_dict)

# 5. Remove Dictionary Item
animals_dict.pop("cat")
print(animals_dict)

# 6. Dictionary Comprehension
animal_lengths_dict = {animal: len(animal) for animal in animals_dict}
print(animal_lengths_dict)

# 7. Nested Dictionary
zoo = {
    "carnivores": {"dog": "canine", "lion": "big cat"},
    "herbivores": {"elephant": "herbivore", "giraffe": "tall herbivore"}
}
print(zoo["carnivores"]["lion"])

# 8. Dictionary Methods
keys = animals_dict.keys()
print(keys)
