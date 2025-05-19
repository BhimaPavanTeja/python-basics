# a="name1"  # Global Scope
# def sample1():
#     # local Scope
#     a="name2"
#     return a
# print(sample1())

# def sample2():
#     return a
# print(sample2())

# def sample3():
#     return a
# print(sample3())



# This function uses global variable s
def f1():
    global s
    s += '!!!'
    print("Inside Function", s)

# Global scope
s = "Hello World"
f1()
print(s)



# # This function uses global variable s
# def f():
#     global s  # Declare that we are using the global variable
#     s += '!!!'
#     print("Inside Function", s)

# # Global scope
# s = "Hello World"
# f()
