def insertion_sort1(arr):
    """
    Insertion sort implementation (my approach #1)

    This implementation creates a new list
    """
    
    sorted_arr = [arr[0]]

    for i in range(1,len(arr)):

        k = 0

        for j in range(len(sorted_arr)):
            
            if arr[i] > sorted_arr[j]:
                k += 1
            else:
                break

        sorted_arr.insert(k, arr[i])

    return sorted_arr

arr =[3,5,4,6,8,1,2,12,41,25]
# print(insertion_sort1(arr))

def insertion_sort2(arr):
    """
    Insertion sort implementation (my approach #2)

    This implementation does not create a new list
    """

    for i in range(1, len(arr)):

        insert_index = 0

        for j in range(0, i):

            if arr[i] > arr[j]:
                insert_index += 1
            else:
                break
        
        arr.insert(insert_index, arr.pop(i))

    return arr


def insertion_sort3(arr):
    """
    textbook implementation (better)
    """
    for i in range(1,len(arr)):

        position = i
        currentvalue = arr[i]
        
        while position > 0 and currentvalue < arr[position-1]:

            arr[position] = arr[position-1]
            position -= 1
        
        arr[position] = currentvalue
    
    return arr


print(arr, "initial")
print(insertion_sort3(arr), "final")