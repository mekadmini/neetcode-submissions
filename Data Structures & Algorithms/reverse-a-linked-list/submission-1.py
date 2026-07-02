# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        prev_elem = head
        curr_elem = head.next
        head.next = None
        while curr_elem:
            next_elem = curr_elem.next
            curr_elem.next = prev_elem
            if not next_elem:
                return curr_elem
            prev_elem = curr_elem
            curr_elem = next_elem
        return curr_elem
        