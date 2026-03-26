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
    
    def _min_value(self,node): # used to find the smallest value in the right tree to serve as a successor when deleting any node with two children
        current = node
        while current.left is not None:
            current = current.left
        return current.data
    
    def delete(self,data):
        self.root = self._delete_recursive(self.root,data)

    def _delete_recursive(self,node,data):
        # base case - value not found
        if node is None:
            return None
        
        #traverse tree to find the node
        if node.data > data:
            node.left = self._delete_recursive(node.left,data)
        elif node.data < data:
            node.right = self._delete_recursive(node.right,data)
        else:
            # case 1 - node has no children
            if node.left is None and node.right is None:
                return None
            
            #case 2 - node has one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # case 3 - node has two children
            successor = self._min_value(node.right)
            node.data = successor
            node.right = self._delete_recursive(node.right,successor)
        return node
