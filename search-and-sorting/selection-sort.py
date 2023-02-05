def selection_sort(arr):
    """
    Selection sort implementation (my approach)
    """

    for i in range(len(arr)-1):

        min_index = i

        # find the index of the smallest element
        for j in range(i,len(arr)):

            if arr[j] < arr[min_index]:

                min_index = j

        # swap
        if arr[min_index] < arr[i]:

            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr

arr = [37,48,23,24,15,25,17,11,25,19]
print(arr, "initial")
print(selection_sort(arr), "final")

        


