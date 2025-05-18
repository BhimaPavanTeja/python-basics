def arrayElementFind(arr: list[int], ele: int) -> list[int]:
    new_array = []
    for e in arr:
        if e != ele:
            new_array.append(e)
    return new_array

array = [2, 1, 2, 3, 4, 5, 6]
print(arrayElementFind(array, 3))
