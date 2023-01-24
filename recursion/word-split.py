def word_split1(phrase,list_of_words, output = None):
    """
    Create a function called word_split() which takes in a string phrase and a 
    set list_of_words. The function will then determine if it is possible to 
    split the string in a way in which words can be made from the list of words. 
    You can assume the phrase will only contain words found in the dictionary if 
    it is completely splittable.

    (non-recursive solution)
    """
    words = []
    curr = ""

    for letter in phrase:

        curr += letter

        if curr in list_of_words:
            words.append(curr)
            curr = ""
    
    return words


def word_split2(phrase,list_of_words, output = None):
    """
    Create a function called word_split() which takes in a string phrase and a 
    set list_of_words. The function will then determine if it is possible to 
    split the string in a way in which words can be made from the list of words. 
    You can assume the phrase will only contain words found in the dictionary if 
    it is completely splittable.

    (recursive solution / textbook solution)
    Note: This is a very python-y solution
    """
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split2(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output        



# print(word_split1('themanran',['the','ran','man']))
# print(word_split1('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
# print(word_split1('themanran',['clown','ran','man']))

print(word_split2('themanran',['the','ran','man']))
print(word_split2('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split2('themanran',['clown','ran','man']))