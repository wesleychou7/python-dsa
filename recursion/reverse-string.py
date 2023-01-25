def reverse(s):
    """
    Reverse a string using recursion
    """
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


print(reverse('hello world'))