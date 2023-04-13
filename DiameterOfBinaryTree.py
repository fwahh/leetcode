from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_height(node: TreeNode) -> Tuple[int, int]:
            if not node:
                return 0, 0
            l_h, l_diameter = get_height(node.left)
            r_h, r_diameter = get_height(node.right)
            return max(l_h, r_h) + 1, max(l_h + r_h, l_diameter, r_diameter)
        
        return get_height(root)[1]