# Tuple() ordered and unchangeable. Duplicates OK. FASTER
my_tuple = (10, 20, 30, 40, 50,20)

count_of_20 = my_tuple.count(20)
print("Count of 20:", count_of_20)  

length_of_tuple = len(my_tuple)
print("Length of tuple:", length_of_tuple)  

my_tuple = (1, 2, 3, 'a', 'b', 'c')
print(my_tuple)
single_element_tuple = (1,)
print("Simple Tuple Declaration",type(single_element_tuple))



empty_tuple = ()
print("Simple Tuple Declaration without comma",type(single_element_tuple))
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])
print(my_tuple[::-1])
 
 
print("slice")
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[::2])

my_tuple = (1, 2, 3, 4)
print(len(my_tuple))
print("hwllo")



tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)



my_tuple = (1, 2)
print(my_tuple * 3)





my_tuple = (1, 2, 3, 4)
print(3 in my_tuple)
print(5 not in my_tuple)


my_tuple = (1, 2, 3,4,5,6)
a, *b, c = my_tuple
print("Type of B",type(b))
print(a, b, c)



my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))#output 3
my_tuple = (1, 2, 4, 3,2)
print(my_tuple.index(2)) #output 1




nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])
print(nested_tuple[1][0])






 


my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)

my_list = [4, 5, 6]
my_tuple = tuple(my_list)
print(my_tuple)





my_tuple = (4, 2, 3, 1)
print(sorted(my_tuple))








my_tuple = (3, 1, 4, 1, 5)
print(max(my_tuple))
print(min(my_tuple))

# Tuple as Return Value
#Returning multiple values from a function using a tuple.
#Example:
def get_values():
    return 1, 2, 3
a, b, c = get_values()
print(a, b, c)      # 1 2 3

