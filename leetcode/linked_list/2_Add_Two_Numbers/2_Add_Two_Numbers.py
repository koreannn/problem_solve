# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # l1값이 남아있으면~
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            curr.next = ListNode(total%10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next


# test
print(Solution().addTwoNumbers([2,4,3], [5,6,4])) # [7,0,8]
print(Solution().addTwoNumbers([0], [0])) # [0]
print(Solution().addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])) # [8,9,9,9,0,0,0,1]