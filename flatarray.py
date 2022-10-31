def flatten_sorter(arr):
    array = []
    for item in arr:
        if type(item) == list:
            for i in item:
                array.append(i)
        else:
            array.append(item)
    return sorted(array)


array1 = [5, 43, [3, 24], 2, 1]
print(flatten_sorter(array1))
