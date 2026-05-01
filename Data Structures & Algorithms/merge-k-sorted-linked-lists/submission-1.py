# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        i = 0 
        for item in lists:
            h.append((item.val, i, item.next))
            i += 1

        heapq.heapify(h)

        op = []
        while h:
            x, i, node = heapq.heappop(h)
            op.append(x)

            if node:
                heapq.heappush(h, (node.val, i, node.next))

        head = None
        tail = None

        for val in op:
            if head == None:
                head = ListNode(val)
                tail = head
            else:
                temp = ListNode(val)
                tail.next = temp
                tail = temp
            
        return head

