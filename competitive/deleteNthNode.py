# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        # Create a dummy node and attach it to the head
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move the first pointer `n + 1` steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next

        # Second pointer is now just before the node to be removed
        second.next = second.next.next

        # Return the new head
        return dummy.next
