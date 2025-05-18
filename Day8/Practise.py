# amount = 196
# notes=[500,100, 50, 20, 10, 5, 2, 1]
# note_count = {}
# for note in notes:
#     if amount >= note:
#         count = amount // note
#         print("Count : ",count)
#         note_count[note] = count
#         amount = amount % note
#         print("Balance Amount : ",amount)
# print("Notes Can Occupy the Amount : ")
# for note, count in note_count.items():
#     print(f"{note} -> {count}")  
# nums = [1,1,1,3]
# target = 6
# def target_sum(nums, target):
#     result = []
#     for start in range(len(nums)):
#         current_sum = 0
#         for end in range(start, len(nums)):
#             current_sum += nums[end]
#             if current_sum == target:
#                 result.append(nums[start:end+1])
#     return result
# print(target_sum(nums, target))
# nums = [1, 2, 4, 6, 7]
# def mis_num(nums):
#     missing = []
#     for num in range(min(nums), max(nums)):
#         if num not in nums:
#             missing.append(num)
#     return missing
# print(mis_num(nums))


# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# def anagram_group(words):
#     anagram_groups = {}
#     for word in words:
#         key = ''.join(sorted(word))
#         if key in anagram_groups:
#             anagram_groups[key].append(word)
#         else:
#             anagram_groups[key] = [word]  
#     print("Group Values ")
#     for k, v in anagram_groups.items():
#         print(f"'{k}' : {v}")
#     return list(anagram_groups.values())
# print()
# print(anagram_group(words))


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






