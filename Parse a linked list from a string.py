class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s=='None':
        return None
    s = s.split(' -> ')[:-1]
    s = [int(i) for i in s][::-1]
    node = Node(s.pop(0))
    for i in range(len(s)):
        node = Node(s[i],node)
    return node
print(linked_list_from_string( "0 -> 1 -> 4 -> 9 -> 16 -> None"))