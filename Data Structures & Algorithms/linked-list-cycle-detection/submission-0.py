# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = 0
        while head:
            head = head.next
            if c > (10 ** 4) + 1:
                return True
            c += 1
        return False

        