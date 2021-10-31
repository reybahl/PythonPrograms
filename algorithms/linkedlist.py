class LinkedList():
    def __init__(self):
        self.headnode = None

    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None
    
    def insert(self, value):
        if self.headnode is None:
            self.headnode = self.Node(value)
            self.lastnode = self.headnode
        else:
            self.lastnode.previous = self.lastnode
            self.lastnode.next = self.Node(value)
            self.lastnode = self.Node(value)

    def print(self):
        if self.headnode is None: 
            print("empty")
        else:
            current_node = self.headnode
        while current_node != self.lastnode:
            
            print(current_node.value, end=", ")
            next_node = current_node.next
            if next_node is None:
                break
            else:
                print(next_node)
            current_node = next_node

linkedlist = LinkedList()
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.print()