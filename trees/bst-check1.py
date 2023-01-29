# textbook solution 

values = []

def inorder(tree):
    """
    Inorder traversal and store each value in a list
    """
    if tree != None:

        inorder(tree.getLeftChild())
        values.append(tree.getRootVal())
        inorder(tree.getRightChild())


def bstCheck(tree):
    """
    Given a binary tree, check whether it’s a binary search tree or not.
    """
    return values == sorted(values)


        


