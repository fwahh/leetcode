from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.fill_vals(root)

    def next(self) -> int:
        return self.vals.pop()
    
    def hasNext(self) -> bool:
        return bool(self.vals)
        
    def fill_vals(self, node):
        if not node:
            return
        if node.right:
            self.fill_vals(node.right)
        self.vals.append(node.val)
        if node.left:
            self.fill_vals(node.left)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()