# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        cur = head
        count = 0
        while cur != None and count < k:
            count += 1
            cur = cur.next
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur  # 不够的情况下直接返回head
        return head
