# def nested_lookup(d, keys):
#     for k in keys:
#         d = d[k]
#     return d
# print(nested_lookup({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']))




    








# def merge_dicts_sum(d1, d2):
#     for k, v in d2.items():
#         if k in d1:
#             d1[k] += v
#         else:
#             d1[k] = v
#     return d1
# print(merge_dicts_sum({'a': 1}, {'a': 2, 'b': 3}))

# def invert_dict(d):
#     inv = {}
#     for k, v in d.items():
#         inv[v] = k
#     return inv
# print(invert_dict({'a': 1, 'b': 2}))

# def char_freq(s):
#     freq = {}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
#     return freq
# print(char_freq('hello'))

# def filter_dict_by_value(d, cond):
#     res = {}
#     for k, v in d.items():
#         if cond(v):
#             res[k] = v
#     return res
# print(filter_dict_by_value({'a': 1, 'b': 2}, lambda v: v > 1))

# def group_by_key(lst):
#     res = {}
#     for item in lst:
#         key = item['key']
#         val = item['value']
#         if key in res:
#             res[key].append(val)
#         else:
#             res[key] = [val]
#     return res
# print(group_by_key([{'key': 'a', 'value': 1}, {'key': 'a', 'value': 2}]))

# def update_nested_dict(d, keys, value):
#     cur = d
#     for k in keys[:-1]:
#         if k not in cur:
#             cur[k] = {}
#         cur = cur[k]
#     cur[keys[-1]] = value
#     return d
# print(update_nested_dict({'a': {}}, ['a', 'b'], 1))

# def dict_from_lists(keys, values):
#     res = {}
#     for i in range(len(keys)):
#         res[keys[i]] = values[i]
#     return res
# print(dict_from_lists(['a', 'b'], [1, 2]))

# def top_k_frequent(d, k):
#     freq_list = []
#     for key, val in d.items():
#         freq_list.append((val, key))
#     freq_list.sort(reverse=True)
#     res = []
#     for i in range(k):
#         res.append(freq_list[i][1])
#     return res
# print(top_k_frequent({'a': 3, 'b': 1, 'c': 2}, 2))

# def flatten_nested_dict(d, parent_key=''):
#     res = {}
#     for k, v in d.items():
#         new_key = parent_key + '.' + k if parent_key else k
#         if isinstance(v, dict):
#             res.update(flatten_nested_dict(v, new_key))
#         else:
#             res[new_key] = v
#     return res
# print(flatten_nested_dict({'a': {'b': 1}}))
# after new


# def keys_with_max_val(d):
#     max_val = None
#     res = []
#     for v in d.values():
#         if max_val is None or v > max_val:
#             max_val = v
#     for k, v in d.items():
#         if v == max_val:
#             res.append(k)
#     return res

# def merge_dicts_mul(dicts):
#     res = {}
#     for d in dicts:
#         for k, v in d.items():
#             if k in res:
#                 res[k] *= v
#             else:
#                 res[k] = v
#     return res

# def is_isomorphic(d1, d2):
#     if len(d1) != len(d2):
#         return False
#     map1 = {}
#     map2 = {}
#     for k1, v1 in d1.items():
#         if k1 in map1:
#             if map1[k1] != v1:
#                 return False
#         else:
#             map1[k1] = v1
#     vals = list(d2.values())
#     if len(set(map1.values())) != len(set(vals)):
#         return False
#     return True

# def missing_keys(d1, d2):
#     res = []
#     for k in d1:
#         if k not in d2:
#             res.append(k)
#     return res

# def group_anagrams(words):
#     res = {}
#     for w in words:
#         key = ''.join(sorted(w))
#         if key in res:
#             res[key].append(w)
#         else:
#             res[key] = [w]
#     return res

# def closest_key(d, target):
#     closest_k = None
#     min_diff = None
#     for k, v in d.items():
#         diff = v - target if v >= target else target - v
#         if min_diff is None or diff < min_diff:
#             min_diff = diff
#             closest_k = k
#     return closest_k

# def key_path_exists(d, keys):
#     for k in keys:
#         if k in d:
#             d = d[k]
#         else:
#             return False
#     return True

# def dot_product(d1, d2):
#     res = 0
#     for k, v in d1.items():
#         if k in d2:
#             res += v * d2[k]
#     return res

# def filter_by_range(d, low, high):
#     res = {}
#     for k, v in d.items():
#         if low <= v <= high:
#             res[k] = v
#     return res

# def invert_dict_list(d):
#     res = {}
#     for k, vals in d.items():
#         for v in vals:
#             res[v] = k
#     return res
