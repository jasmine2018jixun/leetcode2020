# class Solution:
#     """
#     @param: num: An integer
#     @return: An integer
#     """
    # def countOnes(self, num):
    #     # write your code here
    #     s = str(bin(num&int('1'*32, 2)))
    #     count = 0
    #     for i in s:
    #         if i == '1':
    #             count += 1
    #     return count
        
# class Solution:
#     def countOnes(self, n):
#         # write code here
#         count = 0
#         # 负数与0xffffffff相与，消除死循环
#         if n < 0:
#             n = n & 0xffffffff
#         while n:
#             count += 1
#             # 把一个整数减去1，再和原整数做与运算，会把该整数最右边的一个1变成0
#             # 有多少个1就能进行多少次转化
#             n = n & (n-1)
#         return count
        
class Solution:
    def countOnes(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0,32)])

class Solution:
    def countOnes(self, n):
        # write code here
        count = 0
        flag = 1 
        for i in range(32):
            if n & flag:
                count += 1 
            flag = flag << 1 
        return count 