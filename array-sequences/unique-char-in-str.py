def uni_char1(s):
    """
    Given a string, determine if it is comprised of all unique characters. For 
    example, the string 'abcde' has all unique characters and should return 
    True. The string 'aabcde' contains duplicate characters and should return 
    false.
    (My solution #1)
    """

    # edge cases
    if len(s) <= 1:
        return True

    seen = []

    for letter in s:
        if letter not in seen:
            seen.append(letter)
        else:
            return False
    
    return True


def uni_char2(s):
    """
    Given a string, determine if it is comprised of all unique characters. For 
    example, the string 'abcde' has all unique characters and should return 
    True. The string 'aabcde' contains duplicate characters and should return 
    false.
    (Textbook solution #1)
    """

    return len(set(s)) == len(s)


def uni_char3(s):
    """
    Given a string, determine if it is comprised of all unique characters. For 
    example, the string 'abcde' has all unique characters and should return 
    True. The string 'aabcde' contains duplicate characters and should return 
    false.
    (Textbook solution #1)
    """

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    
    return True


# print(uni_char1(''))
# print(uni_char1('goo'))
# print(uni_char1('abcdefg'))
# print(uni_char1('aabcde'))

# print(uni_char2(''))
# print(uni_char2('goo'))
# print(uni_char2('abcdefg'))
# print(uni_char2('aabcde'))

print(uni_char3(''))
print(uni_char3('goo'))
print(uni_char3('abcdefg'))
print(uni_char3('aabcde'))