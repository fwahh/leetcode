from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_vals = []
        q = []
        if root:
            q.append(root)
        
        while q:
            temp = []
            for node in q:
                right = node.val
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            right_vals.append(right)
            q = temp
        return right_vals