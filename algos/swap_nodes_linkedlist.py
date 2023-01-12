from algos import list_node
from algos.list_node import ListNode


class Solution:
    """
    https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the kth node from the beginning and the
    kth node from the end (the list is 1-indexed).

    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
    """
    def getNodesToSwap(self, head: ListNode, k: int) -> tuple[ListNode, ListNode, ListNode, ListNode]:
        """
        return a tuple containing the nodes to swap, and their previous nodes as well.
        (node1, prev1, node2, prev2): prev1 is the previous node that points to node1, etc.
        We can get these nodes throughjust one round of travel. It is easy to get the first node (k from left).
        To get the second node (k from the right): after traveling the first k node, we assume that the current node is the end,
        then the head would be the k node from the right. So each time we advance curr, we advance head as well. When
        we reach the end, then the head is the one k node from the right.!!!!
        """
        first, first_prev, second, second_prev = None, None, None, None
        cur = head
        prev = None
        count = 0
        while cur:
            count += 1
            if count == k:
                first = cur
                first_prev = prev
                second = head
            if count > k:
                second_prev = second
                second = second.next
            prev = cur
            cur = cur.next
        return first, first_prev, second, second_prev

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        first, first_prev, second, second_prev = self.getNodesToSwap(head, k)
        dummy_head = ListNode(-1)
        dummy_head.next = head ## BIG FAN of this dummy head. It helps avoid so many if(s) conditions.
        if not first_prev:
            first_prev = dummy_head
        if not second_prev:
            second_prev = dummy_head

        if first and second:
            if first.next is not second and second.next is not first:
                tmp1 = first.next
                tmp2 = second.next
                first_prev.next = second
                second_prev.next = first
                first.next = tmp2
                second.next = tmp1
            elif first.next == second:
                first_prev.next = second
                tmp = second.next
                second.next = first
                first.next = tmp
            else:
                second_prev.next = first
                tmp = first.next
                first.next = second
                second.next = tmp
            return dummy_head.next # Note: do not return the dummy here
        else:
            return head


if __name__ == '__main__':
    sol = Solution()
    head = list_node.getLinkedList()
    list_node.printLinkedList(head)
    first, first_prev, second, second_prev  = sol.getNodesToSwap(head, 1)
    print(first.val, first_prev.val if first_prev else None, second.val, second_prev.val if second_prev else None)
    print()
    head = sol.swapNodes(head, 4)
    list_node.printLinkedList(head)

