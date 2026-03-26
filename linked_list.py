class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # points to the next node or None if it's the end of the list

class LinkedList:
    def __init__(self):
        self.head = None # empty list has no starting Node

    def insert(self,data):
        # inserts at the head for O(1) performance so no traversal needed to insert
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self,data):
        # traverses from the head until the target value is found OR the end of the list is reached O(n)
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self,data):
        if self.head is None:
            return # nothing to delete if the list is empty
        
        # handles deleting the head note since there is no previous node to replace it
        if self.head.data == data:
            self.head = self.head.next
            return
        
        # traverses list keeping one item behind to correct pointer upon deletion
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next # skips the deleted node
                return
            current = current.next