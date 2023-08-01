"""
Node class defines a single node in the binary search tree. 
Each node contains a value and pointers to left and right child nodes.
"""
class Node:
    """
    Node constructor initializes a node with a value and sets both child pointers to None.
    """
    def __init__(self, value):
        self.value = value  # Value of the node
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node


"""
BinarySearchTree is a binary tree where each node has a value that is greater than the values of all nodes 
in its left subtree and less than the values of all nodes in its right subtree.
"""
class BinarySearchTree:
    """
    The BinarySearchTree constructor initializes an empty binary search tree with the root set to None.
    """
    def __init__(self):
        self.root = None  # Root node of the binary search tree

    """
    Insert method adds a node with a specified value to the binary search tree.
    """
    def insert(self, value):
        # Create a new node with the specified value
        new_node = Node(value)
        # If the binary search tree is empty, set the root to the new node and return True
        if self.root is None:
            self.root = new_node
            return True
        # Temp node used to traverse the tree, starts from the root
        temp = self.root
        while True:
            # If the value already exists in the tree, do not insert and return False
            if new_node.value == temp.value:
                return False
            # If the value is less than the current node's value, go left
            if new_node.value < temp.value:
                # If the current node's left child is None, insert the new node here
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Move to the left child node
                temp = temp.left
            # If the value is greater than the current node's value, go right
            else:
                # If the current node's right child is None, insert the new node here
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Move to the right child node
                temp = temp.right

    """
    Contains method checks if a value exists in the binary search tree.
    """
    def contains(self, value):
        # Temp node used to traverse the tree, starts from the root
        temp = self.root
        while temp is not None:
            # If the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left
            # If the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            # If the value matches the current node's value, return True
            else:
                return True
        # Value is not found in the tree, return False
        return False
    
    def print_tree(self, current_node):
        """
        This method prints the Binary Search Tree in an In-Order manner (Left - Root - Right).
        """
        # If the current node is not None, recursively call print_tree on the left subtree
        if current_node is not None:
            self.print_tree(current_node.left)
            # After traversing the left subtree, print the current node's value
            print(current_node.value)
            # Then, recursively call print_tree on the right subtree
            self.print_tree(current_node.right)

    def print_tree_visual(self, node, level=0):
        """
        This method prints the Binary Search Tree horizontally with root at the top.
        It uses recursion and the level argument to determine the amount of leading spaces.
        """
        if node is not None:
            self.print_tree_visual(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree_visual(node.left, level + 1)
            
    def dfs_pre_order(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
            
        
    
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())