# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import numpy as np
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        mystack = [(root, [root.val])]
        while mystack:
            node, tempt = mystack.pop()
            if node.left is None and node.right is None and np.sum(tempt) == sum:
                res.append(tempt)
            if node.left:
                mystack.append((node.left, tempt+[node.left.val]))
            if node.right:
                mystack.append((node.right, tempt+[node.right.val]))
        return res