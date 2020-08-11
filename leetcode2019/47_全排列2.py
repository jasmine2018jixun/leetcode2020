# 超时
class Solution1:    
    def backtrack(self, res, temp, remain, nums):
        if len(temp) == len(nums) and temp not in res:
            res.append(temp[:])
        else:
            for i in nums:
                if i not in remain:
                    continue
                temp.append(i)
                remain.remove(i)
                self.backtrack(res, temp, remain, nums)
                b = temp.pop()
                remain.append(b)           
                
    def permuteUnique(self, nums):
        res = []
        temp = []
        remain = nums[:]
        self.backtrack(res, temp, remain, nums)
        return res

# 通过
class Solution(object):
    def permuteUnique(self, nums):
        res = []
        temp = []
        remain = nums[:]
        self.cantsubnum(temp, remain, res, nums)
        return res

    def cantsubnum(self, temp, remain, res, nums):
        if len(temp) == len(nums):
            res.append(temp)
        old_nums = [] # 本层循环是否被访问过的数组
        for i in range(len(remain)):
            if remain[i] in old_nums:
                continue
            self.cantsubnum(temp+[remain[i]], remain[0:i]+remain[i+1:], res, nums)
            old_nums.append(remain[i]) 

s = Solution()
print((s.permuteUnique([1, 2, 3])))