class CustomList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self._data.append(item)

    def append(self, item):
        self._data += [item]

    def extend(self, iterable):
        for item in iterable:
            self._data += [item]

    def insert(self, index, item):
        index = max(0, min(index, len(self._data)))
        self._data = self._data[:index] + [item] + self._data[index:]

    def pop(self, index=-1):
        if not self._data:
            raise IndexError("pop from empty list")
        if index < 0:
            index += len(self._data)
        if index >= len(self._data) or index < 0:
            raise IndexError("pop index out of range")
        item = self._data[index]
        self._data = self._data[:index] + self._data[index+1:]
        return item

    def remove(self, value):
        for i in range(len(self._data)):
            if self._data[i] == value:
                self._data = self._data[:i] + self._data[i+1:]
                return
        raise ValueError(f"{value} not in list")

    def clear(self):
        self._data = []

    def count(self, value):
        count = 0
        for item in self._data:
            if item == value:
                count += 1
        return count

    def index(self, value, start=0, end=None):
        end = end if end is not None else len(self._data)
        for i in range(start, min(end, len(self._data))):
            if self._data[i] == value:
                return i
        raise ValueError(f"{value} is not in list")

    def reverse(self):
        self._data = self._data[::-1]

    def sort(self, reverse=False):
        # simple bubble sort for educational purposes
        n = len(self._data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (self._data[j] > self._data[j + 1]) ^ reverse:
                    self._data[j], self._data[j + 1] = self._data[j + 1], self._data[j]

    def copy(self):
        return CustomList(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return CustomList(self._data[index])
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        self.pop(index)

    def __contains__(self, item):
        for value in self._data:
            if value == item:
                return True
        return False

    def __add__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError("can only concatenate CustomList (not other type)")
        return CustomList(self._data + other._data)

    def __mul__(self, times):
        return CustomList(self._data * times)

    def __eq__(self, other):
        if not isinstance(other, CustomList):
            return False
        return self._data == other._data

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"CustomList({self._data})"
