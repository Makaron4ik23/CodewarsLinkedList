class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    listik = []
    if isinstance(node,Node):
        while isinstance(node.next,Node):
            listik.append(node.data)
            node = node.next
        listik.append(node.data)
    listik.append('None')
    return ' -> '.join(str(i) for i in listik)
#