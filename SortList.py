from typing import List, Optional, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case when empty LL or LL of length 1
        if not head or not head.next:
            return head
        
        left, right = self.splitList(head)
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeList(left, right)
    
    def splitList(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        right = slow.next
        slow.next = None
        
        return head, right
    
    def mergeList(self, left: ListNode, right: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        if left:
            cur.next = left
        if right:
            cur.next = right
        
        return head.next
    
    
def printLL(head: ListNode):
    while head:
        print(head.val, end = " ")
        head = head.next
    print()

def createLL(lst: List[int]) -> ListNode:
    head = cur = ListNode()
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next


# head = createLL([6,21,1,3,9,4,5,9,11])
head = createLL([6,21,1,3,9,4,5,9,11])
# left, right = Solution().splitList(head)
# printLL(left)
# printLL(right)
# head = Solution().mergeList(left, right)
# printLL(head)
head = Solution().sortList(head)
printLL(head)