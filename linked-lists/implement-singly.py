class Node (object):
    """
    Implementation of singly linked list
    """
    
    def __init__(self, value) -> None:
        self.value = value
        self.nextnode = None
        self.prevnode = None

    