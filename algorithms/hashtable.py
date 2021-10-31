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

    def insert(self, element_name:str):
        self.table[self.get_index(element_name)].append(element_name)
    
    def contains(self, element_name):
        return (element_name in self.table[self.get_index(element_name)])
    
    def delete(self, element_name):
        index = self.get_index(element_name)
        self.table[index].remove(element_name)
    
    def locate(self, element_name):
        if self.contains(element_name):
            index = self.get_index(element_name)
            next_index = self.table[index].index(element_name)

            print(f"{element_name} found at [{index}][{next_index}]")

        else:
            print("Element not found")

#Tests
mytable  =  HashTable(6)
mytable.insert("Bye")
print(mytable.contains("Bye"))
print(mytable)
mytable.locate("Bye")
mytable.delete("Bye")
mytable.locate("Hello")
