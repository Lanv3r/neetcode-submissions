# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        count = 0
        slow1, fast = head, head
        while fast is not None and fast.next is not None:
            count += 1
            slow1 = slow1.next
            fast = fast.next.next
        #slow1 is at the start of second half
        prev = None
        while slow1 is not None:
            #reverse second half
            tmp = slow1
            slow1 = slow1.next
            tmp.next = prev
            prev = tmp
        #slow1 is at the next pointer of last node
        slow2 = head
        slow1 = prev #slow1 is at the last node
        while slow1:
            res = max(res, slow1.val + slow2.val)
            slow1 = slow1.next
            slow2 = slow2.next
        return res