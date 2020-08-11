#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def find(nums, target):
    d = {}
    def dfs(cur, i, d):
        if i < len(nums) and (cur, i) not in d:
            d[(cur, i)] = dfs(cur + nums[i], i+1, d) + dfs(cur - nums[i], i+1, d)
        return d.get((cur, i), int(cur == target))
    return dfs(0, 0, d)

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    res = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        nums, target = line.split()
        nums = list(nums)
        nums = [int(n) for n in nums]
        target = int(target)
        temp = [nums, target]
        res.append(temp)

    for r in res:
        print(find(r[0][1:], r[1]-r[0][0]))


# def find(nums, target):
#     if sum(nums) < target or (sum(nums) + target) % 2 == 1: return 0
#     P = (sum(nums) + target) // 2
#     dp = [1] + [0 for _ in range(P)]
#     for num in nums:
#         for j in range(P, num-1, -1):dp[j] += dp[j - num]
#     return dp[P]