class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def reverse_linked_list(head, k):
            prev = None
            current = head
            while current and k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev

        count = 0
        current = head
        while current and count < k:
            current = current.next
            count += 1

        if count < k:
            return head

        new_head = reverse_linked_list(head, k)
        head.next = self.reverseKGroup(current, k)

        return new_head
