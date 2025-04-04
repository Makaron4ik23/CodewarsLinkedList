class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    new = Node(None)
    new.data = data
    new.next = head
    return new

def build_one_two_three():
    ott = push(None,3)
    ott = push(ott,2)
    ott = push(ott,1)
    return ott