from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        preOrder = []
        reversePreOrder = []
        def preOrderTraversal(node):
            if node is None:
                preOrder.append(None)
                return
            
            preOrder.append(node.val)
            preOrderTraversal(node.left)
            preOrderTraversal(node.right)
                
        def revPreOrderTraversal(node):
            if node is None:
                reversePreOrder.append(None)
                return
            reversePreOrder.append(node.val)
            revPreOrderTraversal(node.right)
            revPreOrderTraversal(node.left)
        
        preOrderTraversal(root)
        revPreOrderTraversal(root)
        return preOrder == reversePreOrder