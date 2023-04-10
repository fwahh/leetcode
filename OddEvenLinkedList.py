from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        oddHead = odd = head
        evenHead = even = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
            
        odd.next = evenHead
        
        return oddHead
        
        

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

head = createLL([1,2,3,4])
sol = Solution().oddEvenList(head)
printLL(sol)

head = createLL([1,2,3,4,5])
sol = Solution().oddEvenList(head)
printLL(sol)

head = createLL([2,1,3,5,6,4,7])
sol = Solution().oddEvenList(head)
printLL(sol)

