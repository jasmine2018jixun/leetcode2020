# 剑指offer

# 找出所有重复数
test = [0, 3, 1, 0, 3, 1]

def findDuplicates(nums):
    res = []
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == -1:
                break
            if nums[i] == nums[nums[i]]:
                res.append(nums[i])
                nums[i] = -1
                break
            else:
                # 做法1:  死循环
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

                # 做法2:  可行
                a = nums[i] 
                nums[i], nums[a] = nums[a], nums[i]

                # 做法3: 可行
                # nums[nums[i]], nums[i] = nums[i], nums[nums[i]]                  
    return  res

test = [0, 3, 1, 0, 3, 1]
print(findDuplicates(test))


# # leetcode 442
# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         for i in range(len(nums)):
#             while nums[i] != i+1:
#                 if nums[i] == -1:
#                     break
#                 if nums[i] == nums[nums[i]-1]:
#                     res.append(nums[i])
#                     nums[i] = -1
#                     break
#                 else:
#                     a = nums[i] - 1
#                     nums[i], nums[a] = nums[a], nums[i]
#         return res
