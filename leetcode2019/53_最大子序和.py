class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]     
        sum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            maxsum = max(maxsum, sum)
            if sum < 0:
                sum = 0

        return maxsum


