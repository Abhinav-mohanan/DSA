def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False    # for check swapping happended

        # inner loop for comparing adjacent elements
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True

        # if no swaps, array is sorted
        if not swapped:
            break
    return array


array = [12,3,2,33,45,23]
result = bubbleSort(array)
print('sorted list:-',result)