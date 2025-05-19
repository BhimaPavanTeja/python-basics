s = "Hello"
old = s  
print(f"s = {s}, id(s) = {id(s)}")

s += " World"
print(f"New s = {s}, id(s) = {id(s)}")
print(f"Old string still exists as 'old' = {old}, id(old) = {id(old)}")
