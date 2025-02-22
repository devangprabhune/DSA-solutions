from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # Keeps track of nodes at each depth
        i = 0  # Pointer to traverse the string
        
        while i < len(traversal):
            depth = 0
            
            # Count dashes to determine depth
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Read the number (node value)
            val = 0
            while i < len(traversal) and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            # Adjust stack to correct depth
            while len(stack) > depth:
                stack.pop()
            
            # Attach the new node to its parent
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push the new node onto the stack
            stack.append(node)
        
        return stack[0]  # The root node is at the bottom of the stack
    


# import re
# class Solution:
#     def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
#         vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", traversal)][::-1]


#         def fn(level):
#             if not vals or level != vals[-1][0]: return None
#             node = TreeNode(vals.pop()[1])
#             node.left = fn(level+1)
#             node.right = fn(level+1)
#             return node
#         return fn(0)