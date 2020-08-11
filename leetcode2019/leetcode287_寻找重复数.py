# #solution1
# def findDuplicate(nums):
#     for i in range(len(nums)):
#         while nums[i] != i+1:
#             if nums[i] == nums[nums[i]-1]:
#                 return nums[i]
#             else:
#                 temp = nums[i]
#                 nums[i] = nums[nums[i]-1]
#                 nums[temp-1] = temp

# # solution2： floyd判圈
# def findDuplicate(nums):
#     h = nums[0]
#     t = nums[0]
#     while True:
#         h = nums[nums[h]]
#         t = nums[t]
#         if h == t:
#             break
#     pr1 = nums[0]
#     pr2 = t
#     while pr1 != pr2:
#         pr1 = nums[pr1]
#         pr2 = nums[pr2]
#     return pr1


# solution3： 二分法
def findDuplicate(nums):
        left = 1
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid+1
        return right


        
        




print(findDuplicate([1,3,4,2,2]))
