class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    listik = []
    current = head
    while current:
        listik.append(current.data)
        current = current.next
    l1 = [el for i,el in enumerate(listik) if i%2]
    l2 = [el for i,el in enumerate(listik) if not i%2]
    new_head1 = Node(l1[0])
    current = new_head1
    for valik in l1[1:]:
        current.next = Node(valik)
        current = current.next
    new_head = Node(l2[0])
    current = new_head
    for valik in l2[1:]:
        current.next = Node(valik)
        current = current.next
    return Context(new_head,new_head1)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
alternating_split(head)