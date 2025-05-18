nums = [1, 1, 2, 2, 2, 3]
def frequency_sort(nums):
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    nums.sort() 
    def sort_key(x):
        return -freq_dict[x]
    # print(freq_dict.items())
    nums.sort(key=sort_key)  
    # nums = nums[::-1]        
    return nums
print(frequency_sort(nums))