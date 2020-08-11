# 定义链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 两两反转链表
def swapPairs(head):
    thead = ListNode(-1)
    thead.next = head
    c = thead
    while c.next and c.next.next:
        a, b=c.next, c.next.next
        c.next, a.next = b, b.next
        b.next = a
        c = c.next.next
    return thead.next


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
res = swapPairs(head)
while res:
    print(res.val)
    res = res.next