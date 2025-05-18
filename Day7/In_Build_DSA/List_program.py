animals = ["dog", "giraffe", "lion", "elephant", "cat"]
filtered_animals = [
    animal for animal
    in animals if len(animal) >= 5]
filtered_animals.sort()
filtered_animals.reverse()
print(filtered_animals)
