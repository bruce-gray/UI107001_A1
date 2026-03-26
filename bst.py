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
    
    def search(self,data):
        return self._search_recursive(self.root,data)

    def _search_recursive(self,node,data):
        # base case - tree is empty or value is not in tree returns False
        if node is None:
            return False

        # base case - if value found returns True
        if node.data == data:
            return True

        # recursive cases - eliminate essentially half of the tree at each step of the search O(log n)
        if node.data > data:
            return self._search_recursive(node.left,data)
        elif node.data < data:
            return self._search_recursive(node.right,data)
        return False
