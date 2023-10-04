"""
NOT HARDCORE YET, JUST SIMPLE AND BORING

"""

def longestMountain(arr):
    n = len(arr)
    maxLen = 0
    i = 0

    while i < n - 1:
        # Enquanto não estiver subindo, avance.
        while i < n - 1 and arr[i] >= arr[i + 1]:
            i += 1

        start = i

        # Subida
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Descida
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        # Se encontramos uma montanha, atualize maxLen.
        if i != start and i - start + 1 > maxLen:
            maxLen = i - start + 1

    return maxLen

# Testando a função
arr1 = [2, 1, 4, 7, 3, 2, 5]
arr2 = [2, 2, 2]
arr3 = [1,2,3,4,5,6,7,8,6,5,4,3,2,1]
arr4 = [0,0,0,0,1,2,3,4,2,3]

print(longestMountain(arr1))  # Deve imprimir 5
print(longestMountain(arr2))  # Deve imprimir 0
print(longestMountain(arr3))  # Deve imprimir 14
print(longestMountain(arr4))  # Deve imprimir 6
