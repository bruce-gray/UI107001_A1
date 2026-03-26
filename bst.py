class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None # empty tree has no starting node

def insert(self,data):
    self.root = self._insert_recursive(self.root,data)

def _insert_recursive(self,node,data):
    # base case - when empty spot found, place the new node here
    if node is None:
        return Node(data)
    
    # recursive cases - traverses left or right depending on the value
    if data < node.data:
        node.left = self._insert_recursive(node.left,data)
    elif data > node.data:
        node.right = self._insert_recursive(node.right,data)
    return node