#1.超时
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxp = 0
#         for i in range(len(prices)-1):
#             p = max(prices[i+1:]) - prices[i]
#             maxp = max(maxp, p)
#         return maxp


#2.动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p = 9999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p