def sum_array(my_array):
    """
    >>> sum_array([1, 2, 3, 4])
    [1, 3, 6, 10]
        
    >>> sum_array([5, -3, 7])
    [5, 2, 9]

    >>> sum_array([])
    []

    Traceback (most recent call last):
    ...
    ValueError: All elements in the array should be integers or floats.

    """

    if not all(isinstance(i, (int, float)) for i in my_array):
        raise ValueError("All elements in the array should be integers or floats.")

    my_array_sum = []
    sum = 0
    for i in my_array:
        sum += i
        my_array_sum.append(sum)
    return my_array_sum




my_array = []

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    print("Testing completed!")

while True:
    try:
        i = int(input(f"Insert the {len(my_array) + 1}º of the array (-1 to stop): "))
        if i == -1:
            break
        my_array.append(i)
    except ValueError:
        print("A number is required")

print(f"Original array: {my_array}")
print(f"Cumulative sum: {sum_array(my_array)}")



