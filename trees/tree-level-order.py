class Node:

    def __init__(self, val=None):

        self.left = None
        self.right = None
        self.val =  val 


def nextLevelTrees(curr_level_trees):
    """
    Print all values of the trees in curr_level_trees
    Return a list of all child trees of all trees in curr_level_trees
    """

    next_level_trees = []

    for tree in curr_level_trees:

        print(tree.val, end=" ") # print with space in between

        if tree.left:
            next_level_trees.append(tree.left)
        if tree.right:
            next_level_trees.append(tree.right)

    print("") # jump to next line
    
    return next_level_trees
    

def levelOrderPrint(tree):
    """
    Given a binary tree of integers, print it in level order. The output will 
    contain space between the numbers in the same level, and new line between 
    different levels. 
    """
    # first tree (or first node)
    curr_level_trees = nextLevelTrees([tree])

    while curr_level_trees != []:
        curr_level_trees = nextLevelTrees(curr_level_trees)



t = Node(1)

t.left = Node(2)
t.right = Node(3)

t.left.left = Node(4)
t.right.left = Node(5)
t.right.right = Node(6)

levelOrderPrint(t)

    

    



