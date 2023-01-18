def compress1(s):
    """
    Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 
    'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single
    or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even
    though this technically takes more space.

    The function should also be case sensitive, so that a string 'AAAaaa'
    returns 'A3a3'.
    (My solution #1)
    """
    # edge cases
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s + "1"
    
    d = {}
    output = ""

    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    
    for key in d:
        output += key + str(d[key])

    return output


def compress2(s):
    """
    This solution compresses without checking. Known as the RunLength 
    Compression algorithm.
    (textbook solution)
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # edge cases
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    
    return r

# print(compress1(''))
# print(compress1('AABBCC'))
# print(compress1('AAABCCDDDDD'))
# print(compress1('AAAAABBBBCCCC'))
# print(compress1('AAAaaa'))
# print(compress1('AAB'))

print(compress2(''))
print(compress2('AABBCC'))
print(compress2('AAABCCDDDDD'))
print(compress2('AAAAABBBBCCCC'))
print(compress2('AAAaaa'))
print(compress2('AAB'))