# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res_pre = []

    def preorder(self, node):
        if not node:
            return 
        self.res_pre.append(node)
        self.preorder(node.left)
        self.preorder(node.right)
        return self.res_pre
        

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a = self.preorder(root)
        if not a:
            return None
        for i in range(len(a)-1):
            a[i].right = a[i+1]
            a[i].left = None
        return a[0]