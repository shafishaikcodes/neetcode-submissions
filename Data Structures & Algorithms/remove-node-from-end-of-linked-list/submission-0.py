# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        head1 = head
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        pos = 1
        prev = head

        while head:
            # The nth node from the end is at:
            # count - n + 1 position from the beginning.
            if pos == count - n + 1:
                if head == head1:
                    # Removing the first node changes the head.
                    return head1.next

                prev.next = head.next

                # Return the original list head,
                # not the node that was removed.
                return head1
            else:
                prev = head

            # Your code was missing this line,
            # so the loop never moved to the next node.
            head = head.next
            pos += 1

        return head1