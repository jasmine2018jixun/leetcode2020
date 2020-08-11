class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx_left = -1
        idx_right = len(nums)
        idx_current = 0
        while idx_current < idx_right:
            if nums[idx_current] < 1:
                idx_left += 1
                nums[idx_current], nums[idx_left] = nums[idx_left], nums[idx_current]
                idx_current += 1
            elif nums[idx_current] > 1:
                idx_right -= 1
                nums[idx_current], nums[idx_right] = nums[idx_right], nums[idx_current]
            else:
                idx_current += 1

        return nums