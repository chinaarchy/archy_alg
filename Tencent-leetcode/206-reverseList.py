# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 迭代方法
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur, prev = head, None
#         while cur:
#             cur.next, cur, prev = prev, cur.next, cur
#         return prev
# 递归方法
class Solution:
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        if head:
            head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail