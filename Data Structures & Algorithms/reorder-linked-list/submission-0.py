
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        size = 0
        curr = head
        stack = []

        while curr != None:
            stack.append(curr)
            curr = curr.next

        p1 = head
        p2 = stack.pop()

        while p1 != p2 and p1.next != p2:
            temp = p1.next
            p1.next = p2
            p2.next = temp
            p1 = temp
            p2 = stack.pop()

        p2.next = None
        return