from algos import list_node
from algos.list_node import ListNode, printLinkedList


class Solution:
    """
    https://leetcode.com/problems/reverse-nodes-in-k-group/
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list.
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    """
    def reverseGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        cur = head
        cur_group_first = head # first of the current group BEFORE reversal
        dummy_head = ListNode(-1)  # hold the new head for returning
        prev_group_last = dummy_head # last of the prev group AFTER reversal

        count = 0
        while cur and count < k:
            # check if there are enough k elements for a group to reverse
            cur = cur.next
            count += 1
            if count == k:
                (_head, _tail) = self.reverseList(cur_group_first, k)
                prev_group_last.next = _head
                prev_group_last = _tail
                count = 0
                cur_group_first = cur
        while cur_group_first: # the remaining nodes at the end that are not enough to form a group
            prev_group_last.next = cur_group_first
            prev_group_last = cur_group_first
            cur_group_first = cur_group_first.next

        return dummy_head.next # thanks to this dummy head, we don't need to store the new head and avoid many checks.



    def reverseList(self, head: ListNode, k: int) -> tuple[ListNode, ListNode]:
        """
        A support function that reverse k elements in a linked list.
        Return a tuple of new (head, tail)
        """
        prev = None
        cur = head
        count = 0
        while cur and count < k:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            count += 1
        return (prev, head)     # prev becomes the new head, and the old head is the tail

if __name__ == '__main__':
    sol = Solution()
    printLinkedList(sol.reverseGroup(list_node.getLinkedList(), 2))
    printLinkedList(sol.reverseGroup(list_node.getLinkedList(), 3))
