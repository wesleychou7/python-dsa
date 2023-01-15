def finder1(arr1, arr2):
    """
    Given these two arrays, find which element is missing in 
    the second array. (only one element will be missing)
    (My solution #1)
    """

    # edge case
    if abs(len(arr1) - len(arr2)) != 1:
        return "Error"

    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    
    return -1


def finder2(arr1, arr2):
    """
    Given these two arrays, find which element is missing in 
    the second array. (only one element will be missing)
    (My solution #2)
    """

    # edge case
    if len(arr1) - len(arr2) != 1:
        return "Error"


    for i in range(len(arr2)):
        if arr2[i] in arr1:
            arr1.remove(arr2[i])
    
    return arr1[0]


import collections

def finder3(arr1, arr2):
    """
    Given these two arrays, find which element is missing in 
    the second array. (only one element will be missing)
    (Textbook solution #2)
    """
    # using default dict to avoid key errors
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def finder4(arr1, arr2):

    result = 0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2: 
        result ^= num 
        
    return result 



# print(finder1([5,5,7,7],[5,7,7]))
# print(finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder1([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

# print(finder2([5,5,7,7],[5,7,7]))
# print(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

# print(finder3([5,5,7,7],[5,7,7]))
# print(finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder3([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

# print(finder3([5,5,7,7],[5,7,7]))
# print(finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder3([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

print(finder4([5,5,7,7],[5,7,7]))
print(finder4([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
print(finder4([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))