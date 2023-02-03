# sequential search implementation, assuming list is already ordered

def ordered_seq_search(arr,ele):
    """
    Sequential search for an ordered list
    """

    index = 0
    found = False
    stop = False

    while index < len(arr) and not found and not stop:

        if arr[index] == ele:

            found = True

        else:

            if arr[index] > ele:
                stop = True

            else:
                index += 1
    
    return found


