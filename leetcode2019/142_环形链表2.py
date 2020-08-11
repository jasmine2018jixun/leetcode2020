#原理：从链表头节点开始，快慢指针同时开始移动，快指针每次移动2，慢指针每次移动1，若快指针最终与慢指针相遇，则表示链表有环，否则，则为无环。 
#有环情况下，快慢指针相遇时，慢指针位置不变，将快指针置回表头，步长改为每次移1，快慢指针同时开始移动，再次相遇处即为环的入口。


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 存在环
                fast = head # 将快指针退回起点
                while fast != slow: # 快慢指针会在环的入口处相遇
                    fast = fast.next
                    slow = slow.next
                return fast
        return None