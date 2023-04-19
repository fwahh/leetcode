from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def inOrderTraversal(node):
            if len(stack) >= k:
                return
            if node.left:
                inOrderTraversal(node.left)
            stack.append(node.val)
            
            if node.right:
                inOrderTraversal(node.right)
        inOrderTraversal(root)
                
        return stack[k-1]