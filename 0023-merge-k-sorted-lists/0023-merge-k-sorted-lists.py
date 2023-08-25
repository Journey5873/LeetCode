# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        newList = []
        for i in lists:
            while i:
                newList.append(i.val)
                i = i.next

        newList.sort()
        newNode = ListNode()
        head = newNode
        for i in range(len(newList)):
            newNode.next = ListNode(newList[i])
            newNode = newNode.next
        return head.next
