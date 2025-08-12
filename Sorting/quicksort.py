def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left,middle,right = [],[],[]

    # Partition the array into three lists based on comparison with pivot
    for x in array:
        if x < pivot:         # Elements less than pivot
            left.append(x)
        elif x > pivot:       # Elements greter than pivot
            right.append(x)
        else:                 # Elements equal to pivot
            middle.append(x)
    return quick_sort(left) + middle + quick_sort(right)


array = [32,23,4,12,-1,22,3]
result = quick_sort(array)
print(f'sorted list :- {result}')
