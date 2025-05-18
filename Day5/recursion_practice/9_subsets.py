
def subsets(lst: list) -> list:
    if not lst:
        return [[]]
    first = lst[0]
    rest_subsets = subsets(lst[1:])
    return rest_subsets + [[first] + subset for subset in rest_subsets]

print(subsets([1, 2])) 
