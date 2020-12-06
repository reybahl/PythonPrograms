class LinkedList():
    def __init__(self):
        self.headnode = None

    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
    
    
    def insert(self, value):
        if self.headnode is None:
            self.headnode = self.Node(value)
            self.lastnode = self.Node(value)
        else:
            self.lastnode.next = self.Node(value)
            self.lastnode = self.Node(value)

linkedlist = LinkedList()
linkedlist.insert(6)
linkedlist.insert(7)