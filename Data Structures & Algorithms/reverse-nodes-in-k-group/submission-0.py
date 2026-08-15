# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        h1 = head
        last_tail = None
        while h1:
            count = 0
            cur = h1
            while cur and count < k - 1:
                cur = cur.next
                count += 1
            if not cur:
                if last_tail:
                    last_tail.next = h1
                if not new_head:
                    new_head = h1
                return new_head
            else:
                if not new_head:
                    new_head = cur
                h2 = cur.next

                count = 0
                prev = h1
                cur = prev.next
                while count < k - 1:
                    cur.next, cur, prev = prev, cur.next, cur
                    count += 1
                
                if last_tail:
                    last_tail.next = prev
                    print(prev.val)
                last_tail = h1
                h1 = h2
        if last_tail:
            last_tail.next = None
        return new_head
