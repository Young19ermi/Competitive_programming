# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        i = dummyNode
        j = dummyNode.next
        duplicate = float('inf')
        while j:
            if j.val == duplicate:
                i.next = j.next
                j = i.next
            elif j.next and j.val == j.next.val:
                duplicate = j.val
                i.next = j.next.next
                j = i.next
            else:
                i = i.next
                j = j.next
        return dummyNode.next

        
