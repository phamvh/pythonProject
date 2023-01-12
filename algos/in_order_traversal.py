from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    in order traversal
    """

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> list[int]:
        """
        return the list of vals retrieved during the traversal
        """
        if not root:
            return []
        result: list[int] = []
        stack = [root]  # store both int and objects of TreeNode
        while stack:
            node = stack.pop()
            if isinstance(node, int):  # its children were already examined, so just get its value
                result.append(node)
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)  # only add its value, not node, to avoid re-examine its children again
                if node.left:
                    stack.append(node.left)
        return result

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> list[int]:
        ## could be one liner:
        # return inorderTraversalRecursive(root.left) + [root.val] + inorderTraversalRecursive(root.right) if root else []
        if not root:
            return []
        result: list[int] = []
        if root.left:
            result.extend(self.inorderTraversalRecursive(root.left))
        result.append(root.val)
        if root.right:
            result.extend(self.inorderTraversalRecursive(root.right))
        return result
