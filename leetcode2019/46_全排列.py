class Solution:
    # res:最终结果   temp：每个排列
    def backtrack(self, res, temp, nums):
        if (len(temp) == len(nums)):
            res.append(temp[:])
        else:
            for i in nums:
                if i in temp:
                    continue
                temp.append(i)
                self.backtrack(res, temp, nums)
                # print('temp before pop', temp)
                temp.pop() # 遍历下一棵子树'
                # print('temp after pop', temp)

    def permute(self, nums):
        res = []
        temp = []
        self.backtrack(res, temp, nums)
        return res
        

s = Solution()
print(s.permute([1,2,3]))
      
            
