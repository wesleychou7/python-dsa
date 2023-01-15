
def anagram1(s1, s2):
    """
    Given two strings, check to see if they are anagrams
    (My solution)
    """
    # lowercase and remove whitespace
    s1.replace(" ", "").lower()
    s2.replace(" ", "").lower()

    # loop through s1 and check if each charcter is in s2
    # if so, remove that character from s2
    for i in range(len(s1)):

        if s1[i] in s2:
            s2.replace(s1[i], "")
        else:
            return False
    
    return True


def anagram2(s1, s2):
    """
    Given two strings, check to see if they are anagrams
    (Textbook solution)
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # edge case
    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    
    for letter in count:
        if count[letter] != 0:
            return False
    
    return True





# testing

print(anagram1('dog','god'))
print(anagram1('clint eastwood','old west action'))
print(anagram1('aa','bb'))

print(anagram2('dog','god'))
print(anagram2('clint eastwood','old west action'))
print(anagram2('aa','bb'))