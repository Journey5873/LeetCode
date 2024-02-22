class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        new_list = ListNode()
        dummy_head = new_list

        while l1 or l2 or carry:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            
            if l2:
                val += l2.val
                l2 = l2.next

            new_list.next = ListNode(val % 10)
            new_list = new_list.next

            carry = val // 10

        return dummy_head.next