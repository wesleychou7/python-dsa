class Node (object):
    """
    Implementation of doubly linked list
    """
    
    def __init__(self, value) -> None:
        self.value = value
        self.nextnode = None

    