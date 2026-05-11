# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def ll_print(lst):
            ptr = lst
            while ptr:
                print(ptr.val)
                ptr = ptr.next

        def ll_split(head):

            slow, fast = head, head

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            tail = slow.next
            slow.next = None
            return head, tail


        def ll_reverse(head):

            cur = head
            nxt = prv = None

            while cur != None:

                nxt = cur.next
                cur.next = prv

                prv = cur
                cur = nxt

            return prv

        def ll_merge(a, b):
        

            while a and b:

                a_next = a.next
                b_next = b.next

                a.next = b

                if not a_next:
                    break

                b.next = a_next

                a = a_next
                b = b_next


        # 1. Split list
        head, tail = ll_split(head)

        print("split")
        ll_print(head)
        print("tail")
        ll_print(tail)

        # 2. Reverse second half 
        tail = ll_reverse(tail)

        print("rev tail")
        ll_print(tail)

        # 3. Merge
        ll_merge(head, tail)

        print("merge")
        ll_print(head)











