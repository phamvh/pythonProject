class Node:
    def __init__(self, key: int, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root: Node = None
        pass

    def inorder(self, root: Node):
        if not root:
            return
        self.inorder(root.left)
        print(root.key)
        self.inorder(root.right)

    def __insert(self, root: Node, key: int):
        node = Node(key)
        if key < root.key:
            if root.left:
                self.__insert(root.left, key)
            else:
                root.left = node
        elif root.key < key:
            if root.right:
                self.__insert(root.right, key)
            else:
                root.right = node

    def insert(self, key: int) -> None:
        if not self.root:
            self.root = Node(key)
            return
        self.__insert(self.root, key)


    def __inorderSuccessor(self, key: int) -> tuple[Node, Node]:
        """
        Find the inorder successor of a given key.
        Return the successor, and the parent of the successor
        """

    def delete(self, key: int) -> None:
        """
        - if node to be deleted is a leaf, simply remove the leaf
        - if node has only one child, replace the node with its child
        - if not has two children:
              - search for the node's inorder successor. This is easy b/c the node has 2 children. It's the smallest of its right-subtree.
              - copy that successor to the node
              - remove that successor
        - don't forget to update the root if needed
        """
        _root = self.root
        node: Node = None # node to delete
        parent: Node = None # parent of node to delete

        # search for node-to-delete and its parent
        while _root:
            if key < _root.key:
                parent = _root
                _root = _root.left
            elif _root.key < key:
                parent = _root
                _root = _root.right
            elif _root.key == key:
                node = _root
                break
        if not node:
            return # no node found for key

        # deleting ...
        if not node.left and not node.right:
            if parent.left.key == key:
                parent.left = None
            else:
                parent.right = None
            return

        if not node.left:
            if parent.left.key == key:
                parent.left = node.right
            else:
                parent.right = node.right
            return

        if not node.right:
            if parent.left.key == key:
                parent.left = node.left
            else:
                parent.right = node.left
            return

        # node has 2 children, search for its inorder successor (smallest of the right subtree)
        # note that the successor cannot have a left child, otherwise it would not be the smallest of the right substree
        successor = node.right
        successor_parent = node
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # delete the successor
        if successor_parent.left and successor_parent.left.key == successor.key:
            successor_parent.left = None
        elif successor_parent.right and successor_parent.right.key == successor.key:
            successor_parent.right = None

        # copy successor to node
        successor.left = node.left
        if parent.left.key == key:
            parent.left = successor
        else:
            parent.right = successor







