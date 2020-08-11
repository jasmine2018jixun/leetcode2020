def canPartition(nums):
    if len(nums) < 2: return False
    if sum(nums) % 2 == 1: return False
    target = int(sum(nums) / 2)
    dp=[[False]*(target+1) for _ in range(len(nums))]
    dp[0][0] = True
    for i in range(len(nums)):
        dp[i][nums[i]-1] = True
    for i in range(1, len(nums)):
        for j in range(target+1):
            if j >= nums[i]: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            else: dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
print(canPartition([2,2,3,5]))
        

