class Solution:
    def istreeBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True, -1
        isleftBalanced, leftheight = self.istreeBalanced(root.left)
        if not isleftBalanced:
            return False, 0
        isrightBalanced, rightheight = self.istreeBalanced(root.right)
        if not isrightBalanced:
            return False, 0
        return (abs(leftheight-rightheight)<2), 1+max(leftheight, rightheight)
    def isBalanced(self, root: TreeNode) -> bool: 
        return self.istreeBalanced(root)[0]