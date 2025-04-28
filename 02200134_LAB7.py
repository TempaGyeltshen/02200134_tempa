class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print("Created new Binary Tree")
        print(f"Root: {self.root.value if self.root else None}")
    
    def height(self):
        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
    
    def size(self):
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)
    
    def count_leaves(self):
        def _count_leaves(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)
    
    def is_full_binary_tree(self):
        def _is_full(node):
            if node is None:
                return True
            # If it's a leaf node
            if node.left is None and node.right is None:
                return True
            # If both left and right are not None
            if node.left is not None and node.right is not None:
                return _is_full(node.left) and _is_full(node.right)
            # If one child is None and the other isn't
            return False
        return _is_full(self.root)
    
    def is_complete_binary_tree(self):
        # Corrected method name (typo in original)
        def _is_complete(node, index, node_count):
            if node is None:
                return True
            if index >= node_count:
                return False
            return (_is_complete(node.left, 2 * index + 1, node_count)) and \
                   (_is_complete(node.right, 2 * index + 2, node_count))
        
        node_count = self.size()
        return _is_complete(self.root, 0, node_count)
    
    # Corrected version of is_complete_binary_tree (without typo)
    def is_complete_binary_tree(self):
        def _is_complete(node, index, node_count):
            if node is None:
                return True
            if index >= node_count:
                return False
            return (_is_complete(node.left, 2 * index + 1, node_count) and 
                    _is_complete(node.right, 2 * index + 2, node_count))
        
        node_count = self.size()
        return _is_complete(self.root, 0, node_count)

        # Create a sample binary tree
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree = BinaryTree(root)

print(f"Tree Height: {tree.height()}")
print(f"Total Nodes: {tree.size()}")
print(f"Leaf Nodes Count: {tree.count_leaves()}")
print(f"Is Full Binary Tree: {tree.is_full_binary_tree()}")
print(f"Is Complete Binary Tree: {tree.is_complete_binary_tree()}")
