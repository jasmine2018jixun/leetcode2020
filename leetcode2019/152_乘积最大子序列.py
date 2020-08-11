# class Solution:  
#     def maxProduct(self, nums: List[int]) -> int:
#         return max(self.mp(nums), self.mp(nums[::-1]))
    
#     def mp(self, nums: List[int]) -> int:
#         maxm = nums[0]
#         m = 1
#         for i in range(len(nums)):
#             m = m * nums[i]
#             maxm = max(maxm, m)
#             if nums[i] == 0:
#                 m = 1
#         return maxm


class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B)) 