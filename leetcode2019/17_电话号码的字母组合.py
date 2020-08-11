class Solution:
    def letterCombinations(self, digits):
        d = dict()
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'   
        res = []
        temp = ''
        self.dfs(res, temp, digits, d)
        return res
        
    def dfs(self, res, temp, digits, d):
        if len(temp) == len(digits):
            res.append(temp[:])
            temp = ''
        else:
            for i in range(len(digits)):
                for s in d[digits[i]]:
                    temp += s
                    print('temp', temp)
                    self.dfs(res, temp, digits[i+1:], d)
                    # temp = temp[:-1]

s = Solution()
print(s.letterCombinations('234'))