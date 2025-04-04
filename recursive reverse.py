class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    def reverse_helper(cur, prev):
        next_node = cur.next
        cur.next = prev
        return prev if not cur else reverse_helper(next_node, cur)
    return reverse_helper(head, None)
