from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Custom comparator for the heap (min-heap)
        # Python's `heapq` requires the elements to be comparable.
        # To compare `ListNode` objects, we'll use tuples where the first element is the value.
        min_heap = []

        # Add the head of each list to the heap
        for i, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, i, l))  # Add a tuple (value, index, node)

        # Dummy node to start the merged list
        dummy = ListNode(-1)
        tail = dummy

        while min_heap:
            # Get the smallest node from the heap
            _, i, smallest = heappop(min_heap)

            # Add it to the merged list
            tail.next = smallest
            tail = tail.next

            # If the smallest node has a next node, push it into the heap
            if smallest.next:
                heappush(min_heap, (smallest.next.val, i, smallest.next))

        return dummy.next
# Time complexity : O(NlogK)