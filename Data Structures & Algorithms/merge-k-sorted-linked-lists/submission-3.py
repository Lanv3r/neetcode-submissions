# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, tail = None, None
        heap = []
        for h in lists:
            if h is not None:
                heapq.heappush(heap, NodeWrapper(h))
        while heap:
            node_wrapper = heapq.heappop(heap)
            val, next_node = node_wrapper.node.val, node_wrapper.node.next 
            node = ListNode(val, None)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
            if next_node is not None:
                heapq.heappush(heap, NodeWrapper(next_node))

        return head 
        
        