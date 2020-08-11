# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        mystack = [(root, [root.val])]
        while mystack:
            node, tempt = mystack.pop()
            if node.left is None and node.right is None:
                tempt = [str(t) for t in tempt]
                res += int(''.join(tempt))
            if node.left:
                mystack.append((node.left, tempt+[node.left.val]))
            if node.right:
                mystack.append((node.right, tempt+[node.right.val]))
        return res