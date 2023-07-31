# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        temp = 0
        retNode = ListNode()
        head = retNode

        while node1 or node2:
            if node1 and node2 :
                sumNum = node1.val + node2.val + temp
                node1 = node1.next
                node2 = node2.next
            elif node1:
                sumNum = node1.val + temp
                node1 = node1.next
            else:
                sumNum = node2.val + temp
                node2 = node2.next

            if sumNum >= 10:
                sumNum = sumNum % 10
                temp = 1
            else:
                temp = 0

            node = ListNode(sumNum)
            retNode.next = node
            retNode = retNode.next
        if temp != 0:
            node = ListNode(temp)
            retNode.next = node
            retNode = retNode.next
        return head.next