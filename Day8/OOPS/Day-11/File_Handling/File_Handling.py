# File Handling Example

# File path
file_path = "example.txt"
# 1. Create and Write to the File
with open(file_path, "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    print(f"File '{file_path}' created and written successfully.")
# 2. Read from the File
with open(file_path, "r") as file:
    print("Reading file content:")
    content = file.read()
    print(content)
# 3. Append (Update) the File
with open(file_path, "a") as file:
    file.write("This is a new line added in update.\n")
    print(f"File '{file_path}' updated successfully.")
# 4. Read again after updating
with open(file_path, "r") as file:
    print("Reading updated file content:")
    updated_content = file.read()
    print(updated_content)
