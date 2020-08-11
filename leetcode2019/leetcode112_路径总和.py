# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not (root.left or root.right):
            return sum == root.val

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        mystack = [(root, root.val)]
        while mystack:
            node, temp = mystack.pop()
            if node.left is None and node.right is None and sum == temp:
                return True
            if node.left:
                mystack.append((node.left, temp+node.left.val))
            if node.right:
                mystack.append((node.right, temp+node.right.val))
        return False