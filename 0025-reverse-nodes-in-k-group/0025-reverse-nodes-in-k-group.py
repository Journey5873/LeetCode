class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head:
            return head
        tempHead = head
        i = k
        while i:
            tempHead = tempHead.next
            i -= 1
            if not tempHead and i > 0:
                return head
        prev = self.reverseKGroup(tempHead, k)
        node = head
        i = k
        while i:
            next = node.next
            node.next = prev
            prev = node
            if (i==1):
                return node
            node = next
            i -= 1
        return node 