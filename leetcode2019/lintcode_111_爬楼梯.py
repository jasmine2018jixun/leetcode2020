class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            res = [1, 2, 3]
            for i in range(3, n):
                res += [res[i-1] + res[i-2]]
            return res[n-1]