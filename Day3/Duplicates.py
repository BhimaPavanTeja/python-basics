s = "acbac"
s1 = ""
for i in s:
    print(s1.find(i))
    if(s1.find(i) >= 0):
        continue
    else: 
        s1+=i
print(s1)