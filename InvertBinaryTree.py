from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        to_transform = deque()
        to_transform.append(root)
        
        while to_transform:
            cur = to_transform.popleft()
            cur.right, cur.left = cur.left, cur.right
            if cur.right:
                to_transform.append(cur.right)
            if cur.left:
                to_transform.append(cur.left)
                
        return root