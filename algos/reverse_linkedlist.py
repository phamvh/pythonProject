from typing import Optional

from algos.list_node import ListNode, getLinkedList, printLinkedList


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given a linkedlist (the head of the list), reverse the list and return the new head.
    """
    if not head:
        return head

    prev = None
    curr = head
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    return prev

if __name__ == '__main__':
    head = getLinkedList()
    printLinkedList(reverseList(head))
    printLinkedList(reverseList(ListNode(1)))


