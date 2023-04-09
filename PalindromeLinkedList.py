from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = [slow.val]
        # get to middle of LL
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
            
        # if fast.next.next is None => there are odd number of nodes in LL
        if not fast.next:
            stack.pop()
        
        slow = slow.next
        while slow:
            if slow.val != stack[-1]:
                return False
            stack.pop()
            slow = slow.next
            
        return True
    
head = cur = ListNode(1)
for val in [2,2,1]:
    cur.next = ListNode(val)
    cur = cur.next
    
print(Solution().isPalindrome(head))

head = cur = ListNode(1)
for val in [2]:
    cur.next = ListNode(val)
    cur = cur.next
    
print(Solution().isPalindrome(head))

head = cur = ListNode(1)
for val in [1]:
    cur.next = ListNode(val)
    cur = cur.next
    
print(Solution().isPalindrome(head))