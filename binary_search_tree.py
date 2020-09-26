class BinarySearchTree():

    def __init__(self):
        self._node_count = 0
        self._root = None # root node of tree

    class Node():
        # assume that data is not custom type, or else need to implement default operators for less than, greater than or equals to
        def __init__(self, left, right, data): 
            self.data = data
            self._left = left
            self._right = right

    def size(self):
        return self._node_count
    
    def isEmpty(self):
        return self.size() == 0

    # public function for height of BST
    def height(self):
        return self._height(self._root)

    # private recursive function for height of BST
    def _height(self, node):
        if node is None:
            return 0
            
        # add one for every layer of the tree
        return (max(self._height(node.left), self._height(node.right)) + 1)

    # public function for contains
    def contains(self, data):
        return self._contains(self._root, data)

    # private recursive implementation for contains function
    def _contains(self, node, data):
        # base case: reached bottom of tree and value not found
        if node is None:
            return False
                
        if data < node.data:
            # recurse through left subtree because the value we are looking at is smaller than the current value
            return self._contains(node.left, data)
            # recurse through right subtree because the value we are looking at is smaller than the current value
        elif data > node.data:
            return self._contains(node.right, data)

        # found the value we were looking for
        return True

    # public function for add
    def add(self, data):  
        if self.contains(data):
            return False
        else:
            self._root = self._add(self._root, data)
            self._node_count += 1
            return True

    # private recursive function for add function
    def _add(self, node, data):
        # base case: found leaf node, so create new node with data and return
        if node is None:
            node = self.Node(None, None, data)
        else:
            if data < node.data:
                node.left = self._add(node.left, data)
            else:
                node.right = self._add(node.right, data)
        return node

    # public function for remove function
    def remove(self, data):
        if self.contains(data):
            self._remove(self._root, data)
            self._node_count -= 1
        else:
            return False

    # private recursive function for remove function
    def _remove(self, node, data):
        # base case
        if node is None:
            return None

        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            # if no subtrees or only right subtree is present
            if node.left is None:

                node.data = None
                node = None

                return node.right
            # if no subtrees or only left subtree is present
            elif node.right is None: 

                node.data = None
                node = None
                
                return node.left
            # if both subtrees are present, 
            # can choose to take the smallest value of the right subtree or
            # take the largest value of the left subtree to meet the Binary Search Tree Invariant
            # in this case, the former approach is taken
            else:
                node_temp = self._find_min_node(node.right)
                node.data = node_temp.data

                # need to remove duplicate node after reassigning value to the main node to be removed
                self._remove(node.right, node_temp.data)

        return node

    # private function for finding left most node i.e. minimum value node
    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    



    