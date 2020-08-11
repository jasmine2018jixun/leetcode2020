# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    # write code here
    
    if listNode is None:
        return []
    printval = listNode.val

    return printListFromTailToHead(listNode.next) + [printval]

print(printListFromTailToHead(node1))


##### 解法2 设置self.res
class Solution:
    def __init__(self):
        self.res = []
        
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        printval = listNode.val
        self.printListFromTailToHead(listNode.next)
        self.res.append(printval)
        return self.res
######################################################
