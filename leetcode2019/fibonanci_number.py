# def fib(n):
#     nums  = []
#     for i in range(0, n):
#         if i <= 1:
#             nums.append(1)
#         else:
#             nums.append(nums[i-1] + nums[i-2])
#     return nums[n-1]

# 进一步优化内存占用
def fib(n):
    nums  = [1, 1]
    if n <= 2:
        return 1
    else:  
        for i in range(2, n):
            nums[0], nums[1] = nums[1], nums[0]
            nums[1] = nums[0] + nums[1]
    return nums[1]


print(fib(8))


# 如何使得时间复杂度为O(1)?
# 解法：套公式
# 思考：这个公式如何得到，提示：可以转化为矩阵的连乘形式，矩阵连乘可以简化（MATRIX DECOMPOSION)