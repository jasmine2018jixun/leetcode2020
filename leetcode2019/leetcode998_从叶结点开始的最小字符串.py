# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import numpy as np
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = 1e9
        res_list = []
        if not root:
            return ''
        mystack = [(root, [root.val])]
        while mystack:
            node, tempt = mystack.pop()
            if node.left is None and node.right is None:
                    res_list.append(tempt)
            if node.left:
                mystack.append((node.left, tempt+[node.left.val]))
            if node.right:
                mystack.append((node.right, tempt+[node.right.val]))
        res_list = [r[::-1] for r in res_list]
        res_list = sorted(res_list)

        result = []
        for r in res_list[0]:
            result.append(chr(97+dic[r]))
        return ''.join(result)