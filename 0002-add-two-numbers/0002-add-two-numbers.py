# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        retNode = ListNode()
        head = retNode
        carry = 0

        while l1 or l2 or carry:
            sumNum = carry

            if l1:
                sumNum += l1.val
                l1 = l1.next

            if l2:
                sumNum += l2.val
                l2 = l2.next

            carry = sumNum // 10
            sumNum = sumNum % 10

            retNode.next = ListNode(sumNum)
            retNode = retNode.next

        return head.next