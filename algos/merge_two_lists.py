from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    """
    https://leetcode.com/problems/merge-two-sorted-lists/
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    """
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in (list1, list2):
            return list1 or list2

        result: ListNode = None
        head: ListNode = None
        #while (list1 is not None) | (list2 is not None): ---- >>>> this is valid, but not elegant
        while list1 or list2:
            next_min: ListNode
            if list1 is None:
                next_min = list2
                list2 = list2.next
            elif list2 is None:
                next_min = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    next_min = list1
                    list1 = list1.next
                else:
                    next_min = list2
                    list2 = list2.next
            if result is None:
                result = next_min
                head = next_min
            else:
                result.next = next_min
                result = next_min

        return head

    def merge2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        much more elegant
        """
        dummy = curr = ListNode(-1) # just a dummy one to avoid checking for the very first, and also to store the head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # after this while, one of the two lists should be None
        # simply add the entire remaining non-None
        curr.next = list1 or list2
        return dummy.next # discard the dummy one




if __name__ == '__main__':

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node0 = ListNode(0, node3) # head

    node2 = ListNode(2)
    node1 = ListNode(1, node2) # head

    def print_list(node: ListNode):
        while node is not None:
            print(node.val, end=",")
            node = node.next
        print()

    sol = Solution()
    merged = sol.merge(node0, node1)
    print_list(merged)

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node0 = ListNode(0, node3)  # head

    print_list(sol.merge(node0, None))

    ###########
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node0 = ListNode(0, node3)  # head

    node2 = ListNode(2)
    node1 = ListNode(1, node2)  # head
    print_list(sol.merge2(node0, node1))

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node0 = ListNode(0, node3)  # head
    print_list(sol.merge2(node0, None))

