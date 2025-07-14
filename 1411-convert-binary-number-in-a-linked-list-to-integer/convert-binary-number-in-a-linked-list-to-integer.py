# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        s=""

        while head:
            s=s+str(head.val)
            head=head.next

        c=0

        for i in range(len(s)-1,-1,-1):
            c=c+int(s[len(s)-1-i])*(2**i)
            

        return c
        