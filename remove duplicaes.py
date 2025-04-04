class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    listik = []
    while head is not None:
        listik.append(head.data)
        head = head.next
    if not listik:
        return None
    listik = sorted(set(listik))
    head = Node(listik[0])
    current = head
    for item in listik[1:]:
        current.next = Node(item)
        current = current.next
    return head