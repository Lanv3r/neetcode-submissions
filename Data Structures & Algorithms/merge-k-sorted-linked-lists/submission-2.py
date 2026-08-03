# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, prev = None, None
        heap = []
        for h in lists:
            while h is not None:
                heapq.heappush_max(heap, h.val)
                h = h.next
        while heap:
            prev = head
            head = ListNode(heapq.heappop_max(heap), prev)

        return head 
        
        