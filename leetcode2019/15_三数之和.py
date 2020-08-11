# #解法一：暴力搜索（超时）， 遍历三个变量
# class Solution(object):
#     def threeSum(self, nums):
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0:
#                         temp = [nums[i], nums[j], nums[k]]
#                         temp.sort()
#                         if temp not in result:
#                             result.append(temp)
#         return(result)

# 解法二： 遍历一个变量，剩余两个变量用二分搜索：
# class Solution(object):
#     def threeSum(self, nums):
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if -(nums[i] + nums[j]) in nums:
#                     temp = [nums[i], nums[j], -(nums[i]+nums[j])]
#                     temp.sort()
#                     if temp not in result:
#                         result.append(temp)
#         return(result)

#解法二：先排序，然后转化为两数之和问题，nums[i]+nums[j]= -nums[k]（超时）
class Solution(object):
    def sort(self, nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    count += 1
            if count == 0:
                break
        return(nums)

    def twoSum(self, nums1, target):
        result = []
        dic = {}
        for i, num in enumerate(nums1):
            if num in dic:
                result.append([-target-num, num])
            else:
                dic[-target - num] = i
        return result
                        
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i) 
            if self.twoSum(temp, nums[i]):
                for x in self.twoSum(temp, nums[i]):
                    r = [nums[i]]+x
                    # r = self.sort(r)
                    r.sort()
                    if r not in result:
                        result.append(r)
                
        return (result)

if __name__ == "__main__":

    c = Solution()
    print(c.threeSum([-1,0,1,2,-1,-4]))
