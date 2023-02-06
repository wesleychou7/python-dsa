def quick_sort(arr):
    """
    """
  
    
    # base case
    if len(arr) <= 1:
        return arr
    
    # set frontier position to 0 (first element)
    frontier = 0
    
    # sorting
    for i in range(1,len(arr)):
        
        if arr[i] < arr[0]:
            
            frontier += 1
            
            temp = arr[i]
            arr[i] = arr[frontier]
            arr[frontier] = temp
    
    # swap frontier element with element before frontier
    temp = arr[frontier]
    arr[frontier] = arr[0]
    arr[0] = temp
    
    # recursive calls on sublist
    left = quick_sort(arr[:frontier])
    right = quick_sort(arr[frontier+1:])
    
    # combine 
    arr = left + [arr[frontier]] + right
    
    return arr
    
arr = [2,5,4,6,7,3,1,4,12,11]
print(quick_sort(arr))
