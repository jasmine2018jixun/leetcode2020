class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 判断是否有环
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # 找到环的入口
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1