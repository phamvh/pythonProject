from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    """
    https://leetcode.com/problems/balanced-binary-tree/
    Given a binary tree, determine if it is height-balanced

    Height-Balanced
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node
    never differs by more than one.
.
    """

    def __setDepth(self, root: Optional[TreeNode]) -> None:
        """
        recursively set depth attr for each node. Bottom up. O(n)
        """
        if not root:
            return
        if not root.left and not root.right:
            setattr(root, "depth", 1)
            return
        d = 1
        if root.left:
            self.__setDepth(root.left)
            leftd = root.left.depth
            if d < leftd + 1:
                d = leftd + 1
        if root.right:
            self.__setDepth(root.right)
            rightd = root.right.depth
            if d < rightd + 1:
                d = rightd + 1
        setattr(root, "depth", d)

    def __isBalancedRecursive(self, root: Optional[TreeNode]) -> bool:
        """
        call this only after calling the setDepth function.
        Note: it is easy to combine this function with the __setDepth() function above into just one.
        """
        if not root:
            return True
        leftd, rightd = 0,0
        if root.left:
            leftd = root.left.depth
        if root.right:
            rightd = root.right.depth
        if abs(leftd - rightd) > 1:
            return False
        return self.__isBalancedRecursive(root.left) and self.__isBalancedRecursive(root.right)

    def isBalancedTree(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        """
        Simply rewrite the two functions above as one, and need not to set new attr.
        This works bottom-up only once, so complexity is O(n)
        :param root: a tree node
        :return: a tuple, first is if the tree/subtree is balanced or not, and second is its depth.
        """
        if not root:
            return (True, 0)
        if not root.left and not root.right:
            return (True, 1)
        leftd, rightd = 0, 0
        if root.left:
            (left_balanced, leftd) = self.isBalancedTree(root.left)
            # can just return here if not balanced, as we don't need further check
            # like as follows: if not left_balanced: return (False, -1) (don't care about depth anymore)
        if root.right:
            (right_balanced, rightd)  = self.isBalancedTree(root.right)
        depth = 1 + max(leftd, rightd)
        if not left_balanced or not right_balanced:
            return False, depth # don't even need parens here, as it's a tuple by default
        return abs(leftd - rightd) < 2, depth

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.__setDepth(root)
        return self.__isBalancedRecursive(root)

if __name__ == '__main__':
    # tested on leetcode already
    sol = Solution()
    # first, bulky method
    print(sol.isBalanced(None))
    # second, concise method
    print(sol.isBalancedTree(None))[0]