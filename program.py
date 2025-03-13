from datastructures.array import Array

@staticmethod
def merge(array1: "Array", array2: "Array") -> "Array":
    if not isinstance(array1, Array):
        raise TypeError("array1 must be an Array")
    elif not isinstance(array2, Array):
        raise TypeError("array2 must be an Array")

    new_size = len(array1) + len(array2)
    min_length = min(len(array1), len(array2))

    new_array = Array([0]*new_size)  # Initialize with 0's

    # Merging elements from both arrays
    for i in range(min_length):
        new_array.__setitem__(i * 2, array1[i])  # Set items from array1
        new_array.__setitem__(i * 2 + 1, array2[i])  # Set items from array2

    # Handling the remaining elements if the arrays are of unequal length
    index = 2 * min_length
    if len(array1) > len(array2):
        for i in range(min_length, len(array1)):
            new_array.__setitem__(index, array1[i])
            index += 1
    else:
        for i in range(min_length, len(array2)):
            new_array.__setitem__(index, array2[i])
            index += 1

    # Update logical size
    new_array.logical_size = new_size

    return new_array

# Testing with arrays
array1 = Array([5, 7, 17, 13, 11, 12, 12])
array2 = Array([12, 10, 2, 4, 6])

array_calc = merge(array1, array2)
print(array_calc)  # This should now print the merged array
