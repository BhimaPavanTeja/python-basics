def palindrome_check(val:str)->bool:
    result=val
    start=0
    end=len(val)-1
    while(start<end):
        if (result[start]==result[end]):
            start+=1
            end-=1
        else:
            return False
    return True
print(palindrome_check("malayalam"))