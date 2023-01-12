class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
def getLinkedList() -> ListNode:
    node8 = ListNode(8)
    node7 = ListNode(7, node8)
    node6 = ListNode(6, node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    return node1

def printLinkedList(head: ListNode):
    while head:
        print(head.val, end= ",")
        head = head.next
    print()

