def balance_check1(s):
    """
    Given a string of opening and closing parentheses, check whether it’s 
    balanced. We have 3 types of parentheses: round brackets: (), square 
    brackets: [], and curly brackets: {}. Assume that the string doesn’t contain
    any other character than these, no spaces words or numbers. As a reminder, 
    balanced parentheses require every opening parenthesis to be closed in the 
    reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

    You can assume the input string has no spaces.
    (My solution #1)
    """

    # edge case
    if len(s) % 2 != 0:
        return False

    starters = set('{[(')
    matches = {'}':'{', ')':'(', ']':'['}

    stack = []
    
    for paren in s:
        
        if paren in starters:
            stack.append(paren)
        elif len(stack) == 0 or stack.pop() != matches[paren]:
            return False
    
    return True


print(balance_check1('{[()]}'))
print(balance_check1('[](){([[[]]])}('))
print(balance_check1('[{{{(())}}}]((()))'))
print(balance_check1('[[[]])]'))
print(balance_check1('))}][{(('))

        


