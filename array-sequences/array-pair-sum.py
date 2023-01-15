
def pair_sum1(arr, k):
    """
    Given an integer array arr, output all the ** unique ** pairs that 
    sum up to a specific value k.

    For testing purposes, the function outputs the number of pairs instead
    (My solution)
    """

    # edge case
    if len(arr) < 2:
        return "Array needs at least 2 elements"

    pairs = {}

    for i in range(len(arr)):

        if (k - arr[i]) in arr[i+1:]:

            if ( arr[i] not in pairs and 
            arr[i] not in list(pairs.values()) ):

                pairs[arr[i]] = k - arr[i]
    
    return len(pairs)
        
def pair_sum2(arr, k):
    """
    Given an integer array arr, output all the ** unique ** pairs that 
    sum up to a specific value k.

    For testing purposes, the function outputs the number of pairs instead
    (Textbook solution)
    """

    # edge case
    if len(arr) < 2:
        return "Array needs at least 2 elements"
    
    
    seen = set()
    count = 0
    
    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            count += 1
    
    return count

        


print(pair_sum1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum1([1,2,3,1],3))
print(pair_sum1([1,3,2,2],4))

print(pair_sum2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum2([1,2,3,1],3))
print(pair_sum2([1,3,2,2],4))