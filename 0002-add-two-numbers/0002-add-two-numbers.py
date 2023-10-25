# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        retList = ListNode()
        head = retList

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            num = sum % 10
            carry = sum // 10
            retList.next = ListNode(num)
            retList = retList.next
        return head.next