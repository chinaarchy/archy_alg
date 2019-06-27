# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        fast = head
        slow = head

        while fast:
            if fast.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
            if slow == fast:
                return True
        return False