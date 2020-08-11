# 定义链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 翻转链表
#方法1
def backward1(head):
    '''循环法'''
    if head is None:
        print('Error: the nodelist is empty!')
    pre = None
    cur = head
    while cur is not None:
        newhead = cur
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return newhead

#方法2
def backward2(head, newhead):
    '''循环法'''
    if head is None:
        return
    if head.next is None:
        newhead = head
    else:
        newhead = backward2(head.next, newhead)
        following = head.next
        following.next = head
        head.next = None
    return newhead

# test
head = ListNode(1)
p1 = ListNode(3)
p2 = ListNode(5)
p3 = ListNode(7)
p4 = ListNode(9)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
res = backward2(head, None)
while res:
    print(res.val)
    res = res.next


#leetcode206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 迭代法
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        pre = None
        cur = head
        while cur is not None:
            newhead = cur
            tempt = cur.next
            cur.next = pre
            pre = cur
            cur = tempt
        return newhead


    # 递归法
    def reverseList(self, head):
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode
    

