def rev_word1(s):
    """
    Given a string of words, reverse all the words
    (My solution #1)
    """

    return " ".join(reversed(s.split()))


def rev_word2(s):
    """
    Given a string of words, reverse all the words
    (My solution #2, more primitive)
    """

    lst = []
    curr = ""

    for i in range(len(s)):
        
        curr += s[i]

        if (s[i] == " " or i == len(s) - 1) and curr.strip() != "":
            lst.append(curr.strip())
            curr = ""

    output = ""
    for word in reversed(lst):
        output += word + " "
    
    return output[:-1]


def rev_word3(s):
    """
    Given a string of words, reverse all the words
    (My solution #3, even more primitive)
    """

    lst = []
    curr = ""
    
    for i in range(len(s)):
        
        if i < len(s) - 1 and s[i+1] != " ":
            curr += s[i+1]

        elif curr != "":
            lst.append(curr)
            curr = ""

    output = ""
    for i in range(len(lst) - 1, -1, -1):
        output += lst[i] + " "
    
    return output[:-1]


def rev_word4(s):
    """
    Given a string of words, reverse all the words
    (Textbook solution #4)
    """
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))
            


# print(f"'{rev_word2('    space before')}'")
# print(f"'{rev_word2('space after     ')}'")
# print(f"'{rev_word2('   Hello John    how are you   ')}'")
# print(f"'{rev_word2('1')}'")

# print(f"'{rev_word3('    space before')}'")
# print(f"'{rev_word3('space after     ')}'")
# print(f"'{rev_word3('   Hello John    how are you   ')}'")
# print(f"'{rev_word3('1')}'")

print(f"'{rev_word4('    space before')}'")
print(f"'{rev_word4('space after     ')}'")
print(f"'{rev_word4('   Hello John    how are you   ')}'")
print(f"'{rev_word4('1')}'")



