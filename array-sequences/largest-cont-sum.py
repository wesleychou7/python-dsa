def large_cont_sum1(arr):
    """
    Given an array of integers (positive and negative) 
    find the largest continuous sum.
    (My solution / Textbook solution)
    """

    # edge case
    if len(arr) == 0:
        return 0

    max_sum = curr_sum = arr[0]

    for num in arr[1:]:

        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum


def large_cont_sum2(arr):
    """
    Given an array of integers (positive and negative) 
    find the largest continuous sum.
    (My solution / Textbook solution)
    This solution prints the starting index and ending index of the
    continuous sum.
    """

    # edge case
    if len(arr) == 0:
        return 0

    curr_sum = max_sum = arr[0]
    start = end = 0

    for i in range(1, len(arr)):

        if curr_sum < 0:
            start = i

        curr_sum = max(curr_sum + arr[i], arr[i])

        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i

    print(f"Start: {start} , End: {end}")

    return max_sum


# print(large_cont_sum1([1,2,-1,3,4,-1]))
# print(large_cont_sum1([1,2,-1,3,4,10,10,-10,-1]))
# print(large_cont_sum1([-1,1]))
# print(large_cont_sum1([1,-3,2,1,4]))

print(large_cont_sum2([1,2,-1,3,4,-1]))
print(large_cont_sum2([1,2,-1,3,4,10,10,-10,-1]))
print(large_cont_sum2([-1,1]))
print(large_cont_sum2([1,-3,2,1,4]))