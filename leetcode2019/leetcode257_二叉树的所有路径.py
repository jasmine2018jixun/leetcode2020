# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        mystack = [(root, [str(root.val)])]
        while mystack:
            node, tempt = mystack.pop()
            if node.left is None and node.right is None:
                res.append(tempt)
            if node.left:
                mystack.append([node.left, tempt+[str(node.left.val)]])
            if node.right:
                mystack.append([node.right, tempt+[str(node.right.val)]])
        result = []
        for r in res:
            result.append('->'.join(r))
        return result