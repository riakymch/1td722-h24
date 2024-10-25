# Imports
# Nothing to import

class Node(object):
    # Singly linked node
    def __init__(self, name=None, age=None, next=None, prev=None):
        self.name = name
        self.age = age
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # A6
    def append(self, name=None, age=None):
        # Append an item 
        pass
    
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            curr_name = current.name
            curr_age = current.age
            current = current.next
            yield curr_name, curr_age

    def print_foward(self):
        for node in self.iter():
            print(node)   
        
    def search_item(self, val):
         for node in self.iter():
            if val == node:
                return True
         return False
    
    # A7
    def delete(self, value):
        # Delete a node with a specific name
        pass

    # B3 - sort on name
    def sort_list(self):    
        pass    

"""
Trees
"""
# Creating node class
class BST:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = BST(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = BST(data)
                return

# A8: Function to search in BST
    def search(self, val):
        pass 
       
            
    # function to print a BST
    def print_tree(self):
        if self.leftChild:
            self.leftChild.print_tree()
        print( self.data),
        if self.rightChild:
            self.rightChild.print_tree()

# Module main, do not modify
if __name__ == '__main__':
    # LL tests first
    items = DoublyLinkedList()
    items.append('Messi', 10)
    items.append('Ronaldo', 12)
    items.append('Pogba', 22)
    items.append('Jones', 24)
    items.append('Jones', 32)
    items.append('Schmeichel', 55)
    items.append('Ibra', 38)

    print("Original list:")
    items.print_foward()

    items.delete("Jones")
    items.delete("Pogba")
    print("\nList after deleting two items:")
    items.print_foward()

    print("\nList after sorting items on name:")
    items.sort_list()
    items.print_foward()

    # Tree questions next    
    # Creating root node
    root = BST(27)
    # Inserting values in BST
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    # searching the values
    print(root.search(7))
    print(root.search(14))

    root.print_tree()
