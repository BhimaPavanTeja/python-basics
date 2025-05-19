def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}")
            return content
    except FileNotFoundError as er:
        print(f" {file_name} does not exist.")
def modify_file(file_name, new_content):
    try:
        with open(file_name, 'w') as file:
            file.write(new_content)
            print(f"Content of {file_name} has been modified.")
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
def readContent(file_name):
    li=[]
    try:
        with open(file_name, 'r') as file:
            print(li.append(file))
    except FileNotFoundError :
        print("Hello Im Not found")
if __name__ == "__main__":
    file1_content = read_file('file1.txt')
    new_content = "This is the new modified content."
    modify_file('file1.txt', new_content)
    read_file('file1.txt')
    readContent('file1.txt')
