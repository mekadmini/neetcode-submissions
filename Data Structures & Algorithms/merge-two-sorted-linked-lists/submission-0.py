# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        elif list1.val >= list2.val:
            head = ListNode(list2.val)
            list2 = list2.next
        pointer = head
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                pointer.next = ListNode(list2.val)
                list2 = list2.next
            pointer = pointer.next
        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2
        return head


        