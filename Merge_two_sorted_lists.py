class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        if not ptr1:
            return ptr2
        if not ptr2:
            return ptr1
        if ptr1.val <= ptr2.val:
            head = ptr1
            ptr1 = ptr1.next
        else:
            head = ptr2
            ptr2 = ptr2.next
        cur = head

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next

        if ptr1:
            cur.next = ptr1
        elif ptr2:
            cur.next = ptr2
        
        return head
