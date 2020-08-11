# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# example：
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

#解法1 利用切片
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                return ([i, i+1+nums[i+1:].index(target - nums[i])])

#解法2 暴力法：时间复杂度超出限制
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j]+nums[i] == target:
                    return([i,j])

#解法3 一遍 hashmap
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

#解法4 两遍hashmap
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic.keys():
                dic[num] = i 
            else:
                if num == target - num:
                    return(dic[num], i)
        print(dic)
        for i in range(len(nums)):
            if (target-nums[i] in dic.keys()):
                if dic[target-nums[i]]> i:
                    return(i,dic[target-nums[i]])
