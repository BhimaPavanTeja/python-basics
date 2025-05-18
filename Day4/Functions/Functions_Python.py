
def sample():
    print("Hello Idiot")
    return 1
print(sample())

def sample2(name):
    print(f"hello mr/mrs. {name}")
print(sample2("Sankara"))


def sample3(first_name,last_name):
    return f"hello MR/MRS {first_name} {last_name} age :{100}"
print(sample3("Sankaranarayanan","Srinivasan"))


def increment(number,by=12):
    result=number+by
    return result
result1=increment(6)
print(result1)


def multiple_values(*number):
    total=1
    for numbers in number:
        total*=numbers
    return total
print((type)(multiple_values(2,3,4,5,6,6)))
print((multiple_values(2,3,4,5,6,6)))

def number_Of_arguments(**values):
    print(values["id"],values["name"],values["age"])
number_Of_arguments(name="Murali",id=1,age=30)

# message1=1
# def global_scope(value):
#      global message1
#      message1=3
#      return f" {value}  {message1 }"
# print(global_scope("this is number from global variable"))



    