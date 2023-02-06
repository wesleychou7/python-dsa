def shell_sort(arr):
    """
    Shell sort implementation (my approach)
    """
    interval = len(arr) // 2

    while interval > 0:

        for i in range(interval, len(arr)):

            position = i
            currentvalue = arr[i]
            
            while position > 0 and currentvalue < arr[position-interval]:

                arr[position] = arr[position-interval]
                position -= interval
            
            arr[position] = currentvalue       
        
        interval //= 2
    
    return arr

arr = [9, 8, 3, 7, 5, 6, 4, 1]

print(shell_sort(arr))
