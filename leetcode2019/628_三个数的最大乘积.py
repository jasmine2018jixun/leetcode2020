class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        # nums = self.quick_sort(nums)
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
    
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        left = []
        right = []
        mid = []
        for i in range(len(nums)):
            if nums[i] < nums[-1]:
                left.append(nums[i])
            elif nums[i] > nums[-1]:
                right.append(nums[i])
            else:
                mid.append(nums[i])
        return self.quick_sort(left) + mid + self.quick_sort(right)

