def bubble_sort1(arr):
    """
    Bubble sort implementation (first attempt)
    """

    end = len(arr)
    allsorted = False

    while not allsorted:

        counter = 0

        for i in range(end):

            if i + 1 != end and arr[i] > arr[i+1]:

                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

                counter += 1
        
        end -= 1
        if counter == 0:
            allsorted = True
    
    return arr

arr = [67,9,4,2,10,32,99,10,1,3,50,23]
# print(bubble_sort1(arr))


def bubble_sort2(arr):
    """
    Bubble sort implementation (textbook solution)
    
    Note: My solution is actually better because it stops as soon as the list 
    is sorted. It does not continue checking the already sorted list like the
    textbook solution does.
    """

    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        #
        for k in range(n):
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

    return arr

print((bubble_sort2(arr)))