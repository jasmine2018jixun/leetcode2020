"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        mystack = [root]
        res = []
        while mystack:
            queque = []
            tempt = []
            for node in mystack:
                tempt.append(node.val)
                if node.children:
                    queque += node.children
            res.append(tempt)
            mystack = queque
        return res
