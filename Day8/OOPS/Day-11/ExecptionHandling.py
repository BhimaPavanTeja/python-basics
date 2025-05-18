def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of division is: {result}")
    finally:
        print("Division operation is complete.")
divide_numbers(0,1)
divide_numbers(1,0)
        
        
        
        
        
        
        
        
        
        
        

# def access_list_element(my_list, index):
#     try:
#         print(f"Accessing element at index {index}: {my_list[index]}")
#     except IndexError:
#         print("Error: Index out of range.")
#     finally:
#         print("List access operation is complete.")

# def convert_to_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         print(f"Error: Cannot convert '{value}' to an integer.")

# def open_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             data = file.read()
#             print(f"File content: {data}")
#     except FileNotFoundError:
#         print(f"Error: The file '{file_name}' was not found.")
#     except IOError:
#         print(f"Error: Cannot read the file '{file_name}'.")
#     finally:
#         print("File operation is complete.")

# def raise_custom_exception(age):
#     try:
#         if age < 18:
#             raise ValueError("Age must be 18 or older.")
#         print(f"Access granted. Your age is: {age}")
#     except ValueError as ve:
#         print(f"Custom Error: {ve}")

# # Test functions with exception handling
# divide_numbers(10, 2)  # Normal case
# divide_numbers(10, 0)  # ZeroDivisionError

# my_list = [1, 2, 3, 4]
# access_list_element(my_list, 2)  # Normal case
# access_list_element(my_list, 5)  # IndexError

# print(f"Converted value: {convert_to_int('42')}")  # Normal case
# convert_to_int('abc')  # ValueError

# open_file('example.txt')  # FileNotFoundError

# raise_custom_exception(20)  # Normal case
# raise_custom_exception(16)  # Custom exception
