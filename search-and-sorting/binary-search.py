# implementation of binary search, assuming list is already ordered

def binary_search1(arr, ele):

    first = 0
    last = len(arr) - 1

    found = False

    while not found and first <= last:

        mid = (first + last) // 2

        if arr[mid] == ele:

            return True

        else:

            if ele > arr[mid]:
                first = mid + 1
            else:
                last = mid - 1
    
    return found  

arr = [1,2,3,4,5,6,7,8,9,10]
# print(binary_search1(arr, 5))



# using recursion

def binary_search2(arr, ele):

    if len(arr) == 0:
        return False
    
    else:

        mid = len(arr) // 2

        if ele == arr[mid]:
            return True

        else:

            if ele < arr[mid]:
                return binary_search2(arr[:mid], ele)

            else:
                return binary_search2(arr[mid+1:], ele)

print(binary_search2(arr, 7))