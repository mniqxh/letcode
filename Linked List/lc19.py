# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    Given a linked list, remove the n-th node from the end of list and return its head.
    Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:
    Given n will always be valid.
    Follow up:
    Could you do this in one pass?

    给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。
    示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
    给定的 n 保证是有效的。
    进阶：
    你能尝试使用一趟扫描实现吗？
    '''

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy
        while first:
            if n < 0:
                second = second.next
            first = first.next
            n -= 1
        if second.next:
            second.next = second.next.next

        return dummy.next
