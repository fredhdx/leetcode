#Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def merge(arr1, arr2):
    i, j = 0, 0  # arr1, arr2
    output = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    while i < len(arr1):
        output.append(arr1[i])
        i += 1

    while j < len(arr2):
        output.append(arr2[j])
        j += 1

    return output

    

    
