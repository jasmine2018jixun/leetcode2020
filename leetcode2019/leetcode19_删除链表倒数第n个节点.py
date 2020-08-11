# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return 
        mystack = []
        node = head
        while node:
            mystack.append(node)
            node = node.next
        if n == len(mystack):
            head = head.next
            return head
        else:
            mystack[-(n+1)].next = mystack[-n].next
            return head