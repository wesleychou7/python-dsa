class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


def cycle_check1(node) -> bool:
    """
    Given a singly linked list, write a function which takes in the first node 
    in a singly linked list and returns a boolean indicating if the linked list 
    contains a "cycle".

    A cycle is when a node's next point actually points back to a previous node 
    in the list. This is also sometimes known as a circularly linked list.
    (textbook solution)
    """
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return True
    
    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)
w = Node(4)

x.nextnode = y
y.nextnode = z
z.nextnode = w


print(cycle_check1(a))
print(cycle_check1(x))
