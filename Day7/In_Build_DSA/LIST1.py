# # LIST EXAMPLES
# # 1. Creating a List
# animals = ["dog", "cat", "elephant", "lion"]
# print(animals)

# # 2. Access List Items
# print(animals[0])  

# # 3. Change List Items
# animals[1] = "tiger"
# print(animals)

# # 4. Add List Items
# animals.append("zebra")
# print(animals)

# # 5. Insert Item at Specific Index
# animals.insert(2, "giraffe")
# print(animals)

# # 6. Remove List Items
# animals.remove("lion")
# print(animals)

# # 7. Pop Last Item
# last_animal = animals.pop()
# print("this is from pop fuc")
# print(last_animal)

# # 8. Sort List
# animals.sort()
# print(animals)

# # 9. Reverse List
# animals.reverse()
# print(animals)

# # 10. List Comprehension
# animal_lengths = [len(animal) for animal in animals]
# print(animal_lengths)




Sample=[0,1,2,3,4,5,6]
print(len(Sample))
print(Sample[::2])
print(Sample[0:2])
print(Sample[-3:-1])


# my_list = [10, 20, 30, 40, 50]
# print(my_list[-3:])  
# print(my_list[-2]) 




my_list = [10, 20, 30, 40, 50]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [50, 40, 30, 20, 10]


