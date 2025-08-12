def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1    # index of the last element in the sorted part
        """
        Move elements of sorted part that are greater
        than key to one position ahead
        """
        while j >=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

array = [12,32,1,3,2,-1]
result = insertionSort(array)
print("sorted list:- ",result)