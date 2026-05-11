# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode(0)

        cur = dummy

        carry = 0

        while ptr1 and ptr2:
            cur.next = ListNode((ptr1.val + ptr2.val + carry) % 10)
            cur = cur.next

            carry = ((ptr1.val + ptr2.val + carry) // 10)
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        leftover = ptr1 or ptr2
        while leftover:
            cur.next = ListNode((leftover.val + carry) % 10)
            cur = cur.next
            carry = (leftover.val + carry) // 10
            leftover = leftover.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next

