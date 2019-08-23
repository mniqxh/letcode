# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Given a non-empty, singly linked list with head node head, return a middle node of linked list.
    If there are two middle nodes, return the second middle node.

    给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
    如果有两个中间结点，则返回第二个中间结点
    """

    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
