class HashTable():
    

    def __init__(self, length):
        self.length = length
        self.table = [[] for i in range(length)]
    
    def get_index(self, element):
        self.hashcode = hash(element)
        self.index = self.hashcode % self.length

        return self.index
        
    def __str__(self):
        return str(self.table)

    def insert(self, element):
        self.table[self.get_index(element)].append(element)
    
    def contains(self, element_name):
        return (element_name in self.table[self.get_index(element_name)])

mytable  =  HashTable(6)
mytable.insert("Hello")
print(mytable.contains("Bye"))
print(mytable)