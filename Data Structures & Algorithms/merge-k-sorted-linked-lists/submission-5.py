# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    tail = tail.next
                    l1 = l1.next
                else:
                    tail.next = l2
                    tail = tail.next
                    l2 = l2.next
            while l1:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            while l2:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            return dummy.next

        while len(lists) > 1:
            mergedLists = []
            i = 0
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
                i += 2
            lists = mergedLists

        return lists[0]
        