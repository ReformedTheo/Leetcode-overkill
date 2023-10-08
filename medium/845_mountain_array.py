from typing import List

def longestMountain(arr: List[int]) -> int:
    """
    Returns the length of the longest 'mountain' in an array. A mountain is defined as a sequence 
    of numbers that first rise and then fall.
    
    Parameters:
    - arr: List[int]: A list of integers.

    Returns:
    - int: The length of the longest mountain found in the array.
    
    Examples:
    >>> longestMountain([2, 1, 4, 7, 3, 2, 5])
    5
    >>> longestMountain([2, 2, 2])
    0
    >>> longestMountain([1,2,3,4,5,6,7,8,6,5,4,3,2,1])
    14
    >>> longestMountain([0,0,0,0,1,2,3,4,2,3])
    6
    """
    
    n = len(arr)
    maxLen = 0
    i = 0

    while i < n - 1:
        # While not ascending, move forward.
        while i < n - 1 and arr[i] >= arr[i + 1]:
            i += 1

        start = i

        # Ascent
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Descent
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        # If we found a mountain, update maxLen.
        if i != start and i - start + 1 > maxLen:
            maxLen = i - start + 1

    return maxLen

# Allow user to input data and print results
def user_input_and_print():
    # Taking user input as a comma-separated string, then converting it to a list of integers
    user_data = list(map(int, input("Enter a list of integers separated by commas (e.g., 2,1,4,7,3,2,5): ").split(',')))
    
    # Call the function and print the result
    result = longestMountain(user_data)
    print(f"The length of the longest mountain in the given data is: {result}")

# Testing the function via docstrings
if __name__ == "__main__":
    user_input_and_print()
    import doctest
    doctest.testmod(verbose=True)
