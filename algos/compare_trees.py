from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/same-tree/description/
    Same structures and same values
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False;
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            n1 = stack1.pop()
            n2 = stack2.pop()
            if n1.val != n2.val:
                return False
            if n1.left and n2.left:
                stack1.append(n1.left)
                stack2.append(n2.left)
            elif (n1.left and not n2.left) or (not n1.left and n2.left):
                return False
            if n1.right and n2.right:
                stack1.append(n1.right)
                stack2.append(n2.right)
            elif (n1.right and not n2.right) or (not n1.right and n2.right):
                return False
        if stack1 or stack2:
            return False
        return True

    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val ==q.val and self.isSameTreeRecursive(p.left, q.left) and self.isSameTreeRecursive(p.right, q.right)
        else:
            return p == q # only True if both are None; else False
