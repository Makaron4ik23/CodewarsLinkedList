class Node:
    def __init__(self, next=None):
        self.next = next

def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return 0
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    length = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        length += 1
    return length