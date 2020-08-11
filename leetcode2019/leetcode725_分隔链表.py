class Solution:
    def split(self, length, k):
        base = length // k
        remain = length % k
        print(remain)
        res = [base]*k
        while remain > 0:
            res[remain-1] += 1
            remain -= 1
        return res

    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [None]*k
        length = 0
        node = root
        while node:
            length += 1
            node = node.next
        nums = self.split(length, k)
        i = 0
        res = []
        temp = root
        while i < k:
            n = nums[i]
            j = 0
            root_i = ListNode(-1)
            temp_j = root_i
            while j < n:
                temp_j.next = temp
                temp = temp.next
                temp_j = temp_j.next
                j += 1
            temp_j.next = None
            res.append(root_i.next)
            i += 1
        return res