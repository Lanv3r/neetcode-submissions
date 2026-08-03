# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, tail = None, None
        new_lists = []
        #append new head to each list
        for h in lists:
            if h is not None:
                new_head = ListNode(0, h)
                new_lists.append(new_head)

        while new_lists:
            #find min
            cur_min = float('inf')
            ind = -1
            for i in range(len(new_lists)):
                val = new_lists[i].next.val
                if val < cur_min:
                    ind = i
                    cur_min = val
            #append node to the result
            node = ListNode(cur_min, None)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
            #delete node from the original list
            node_to_delete = new_lists[ind].next
            if node_to_delete.next is None:
                new_lists.pop(ind) #if it was last node in the list
            else:
                new_lists[ind].next = node_to_delete.next #point to next node in the list

        return head 
        
        