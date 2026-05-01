
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop

class Solution:
    def mergeKLists(self, lists):
        # Seed the heap with the head of each non-empty list
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head is not None]
        heapify(heap)

        dummy = ListNode()   # sentinel; dummy.next will be the real head
        tail = dummy

        while heap:
            val, i, node = heappop(heap)
            tail.next = node
            tail = node
            if node.next is not None:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
            




