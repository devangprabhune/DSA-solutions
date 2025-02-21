from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # Store all recovered values
        self.recover_tree(root, 0)  # Start recovery from root with value 0

    def recover_tree(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val  # Restore node's correct value
        self.values.add(val)  # Store in set for fast lookup
        
        # Recursively recover left and right children
        self.recover_tree(node.left, 2 * val + 1)
        self.recover_tree(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values  # O(1) lookup
