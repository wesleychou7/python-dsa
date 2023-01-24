
class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


def reverse1(head):
    """
    Write a function to reverse a Linked List in place. The function will take 
    in the head of the list as input and return the new head of the list.
    (my solution #1; NOT O(1) space)
    """ 
    lst = [head]
    marker = head

    while marker.nextnode != None:
        lst.append(marker.nextnode)
        marker = marker.nextnode
    
    lst = list(reversed(lst))

    for i in range(len(lst)):
        if i != len(lst) - 1:
            lst[i].nextnode = lst[i+1]
    
    head.nextnode = None
        
    return lst[0]


def reverse2(head):
    """
    Write a function to reverse a Linked List in place. The function will take 
    in the head of the list as input and return the new head of the list.
    (textbook solution #1; O(1) space)
    """ 
    
    current = head
    previous = None
    next = None

    while current:

        next = current.nextnode

        current.nextnode = previous

        previous = current
        current = next

    return previous



# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
# d.nextnode.value # This will give an error since it points to None

reverse2(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
# print(a.nextnode.value) # This will give an error since it now points to None