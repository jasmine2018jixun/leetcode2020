# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(node):
    while node:
        print(node.val)
        node = node.next
# class Solution:
def addTwoNumbers(l1: ListNode, l2: ListNode):
    temp1 = []
    temp2 = []
    while l1:
        temp1.append(l1.val)
        l1 = l1.next
    while l2:
        temp2.append(l2.val)
        l2 = l2.next
    n1 = sum([temp1[i]*(10**i) for i in range(len(temp1))])
    n2 = sum([temp2[i]*(10**i) for i in range(len(temp2))])
    n3 = n1 + n2
    n3 = list(str(n3))
    flag = 0
    for i in n3[::-1]:
        if flag == 0:
            res = ListNode(int(i))
            flag += 1
        else:
            p = res 
            while p.next:
                p = p.next
            p.next = ListNode(int(i))

    return res



l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13
l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l21.next = l22
l22.next = l23
printlist(addTwoNumbers(l11, l21))