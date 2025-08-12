def selectionSort(array):
    n = len(array)  
    for i in range(n):

        # Assume the current position holds minimum element
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:

                # update min_index if a smaller element found
                min_index = j
        
        # move minimum element to its correct position
        array[min_index],array[i] = array[i],array[min_index]
    return array

array = [12,32,3,34,1,3,-2]
result = selectionSort(array)
print('sorted array:-',result)