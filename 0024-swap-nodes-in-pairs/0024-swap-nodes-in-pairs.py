# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        ret = head.next
        prev, curr = None, head
        while curr and curr.next:
            next = curr.next
            temp = next.next
            next.next = curr
            curr.next= temp
            if prev:
                prev.next = next
            prev = curr
            curr = temp
        
        return ret