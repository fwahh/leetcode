from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = ahead = head
        for _ in range(n):
            ahead = ahead.next
        
        # consider edge case when n is the length of list
        if ahead == None:
            return head.next
        
        while ahead.next:
            cur = cur.next
            ahead = ahead.next
            
        # cur is now the n + 1th node from end of list
        prev = cur
        prev.next = cur.next.next
            
        return head
    
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

for n in (5, 1, 2):
    head = createLL([1,2,3,4,5])
    sol = Solution().removeNthFromEnd(head, n)
    printLL(sol)
