class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if index<0:
        raise AttributeError("Invalid index value should throw error.")
    if not isinstance(node,Node):
        raise ValueError("None linked list should throw error.")
    try:
        for i in range(index):
            node = node.next
    except AttributeError:
        raise AttributeError("Invalid index value should throw error.")
    except IndexError:
        raise AttributeError("Invalid index value should throw error.")
    return Node(node.data)
print(get_nth(Node(1, Node(2, Node(3, None))),0).data)