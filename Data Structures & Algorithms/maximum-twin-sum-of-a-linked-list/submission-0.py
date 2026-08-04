# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        count = 0
        val = {}
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            val[count] = slow.val
            count += 1
            slow = slow.next
            fast = fast.next.next
        n = 2 * count
        while slow is not None:
            res = max(res, slow.val + val[n - 1 - count])
            slow = slow.next
            count += 1
        return res