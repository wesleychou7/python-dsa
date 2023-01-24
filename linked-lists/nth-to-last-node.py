class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


def nth_to_last_node(n, head):
    """
    Write a function that takes a head node and an integer value n and then 
    returns the nth to last node in the linked list.
    """

    current = head
    length = 0

    while current:
        length += 1
        current = current.nextnode
    current = head

    # edge case
    if n > length:
        raise LookupError("Error: n is larger than the linked list")

    for i in range(length - n):
        current = current.nextnode

    return current



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 
print(target_node.value)