# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        mergeList = ListNode()
        head = mergeList

        while list1 and list2:
            if list1.val <= list2.val:
                mergeList.next = ListNode(list1.val)
                list1 = list1.next
            else:
                mergeList.next = ListNode(list2.val)
                list2 = list2.next
            mergeList = mergeList.next
        
        while list1:
            mergeList.next = ListNode(list1.val)
            list1 = list1.next
            mergeList = mergeList.next

        while list2:
            mergeList.next = ListNode(list2.val)
            list2 = list2.next
            mergeList = mergeList.next
        
        return head.next