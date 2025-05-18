def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}")
            return content
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
def modify_file(file_name, new_content):
    try:
        with open(file_name, 'w') as file:
            file.write(new_content)
            print(f"Content of {file_name} has been modified.")
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
if __name__ == "__main__":
    file1_content = read_file('file1.txt')
    new_content = "This is the new modified content."
    modify_file('file1.txt', new_content)
    read_file('file1.txt')
if __name__ =="__main__":
    file1_content= read_file('file.txt')
    new_conten =read_file('file12.txt')
    old_content="Blocks Working without any error"
    modify_file('file1.txt',old_content)
    read_file('file1.txt')