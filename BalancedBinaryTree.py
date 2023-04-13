from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height_balance(node: TreeNode) -> Tuple[int, bool]:
            if not node:
                return 0, True
            l_h, l_bal = get_height_balance(node.left)
            r_h, r_bal = get_height_balance(node.right)
            return max(l_h, r_h) + 1, abs(l_h - r_h) <= 1 and l_bal and r_bal
        return get_height_balance(root)[1]