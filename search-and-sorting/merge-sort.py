def merge_sort(arr):
    """
    Implementation of merge sort
    """

    # base case
    if len(arr) > 1:

        # split arr
        mid = len(arr) // 2

        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        # recursive call
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # merge
        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            
            else:
                arr[k] = righthalf[j]
                j += 1
                
            k += 1

        # add leftovers
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr


arr = [11,2,5,4,7,6,8,1,23,1,7,90,90,55]
print(merge_sort(arr))