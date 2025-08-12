def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2

    # Recursively sort the left half
    left = merge_sort(array[:mid])

    # Recursively sort the right half
    right = merge_sort(array[mid:])

    # merge sorted halves   
    return merge(left,right)

def merge(array1,array2):
    result = []
    left = right = 0

    # compare element and append smaller one
    while left < len(array1) and right <len(array2):
        if array1[left] < array2[right]:
            result.append(array1[left])
            left += 1
        else:
            result.append(array2[right])
            right += 1
    
    # append remaining elements
    if left < len(array1):
        result.extend(array1[left:])
    if right < len(array2):
        result.extend(array2[right:])

    return result

array = [23,4,5,34,65,44,1]
result = merge_sort(array)
print('sorted list:- ',result)

    