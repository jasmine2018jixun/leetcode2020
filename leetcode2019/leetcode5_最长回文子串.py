## 1、暴力枚举法
# def longestPalindrome(s):
#     if not s: return False
#     max_len = 1
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if j-i+1 > max_len and _huiwen(s[i:j+1]):
#                 res = s[i:j+1]
#                 max_len = j-i+1
#     return res

# def _huiwen(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(longestPalindrome("babad"))

# 2、动态规划法

def longestPalindrome(s):
    if not s: return s
    if len(s) < 2: return s
    max_len = 0
    res_l = 0
    res_r = 0
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for l in range(len(s)):
        for r in range(l, len(s)):
            if r == l:
                dp[l][r] = True
            elif r == l + 1:
                if s[l] == s[r]: dp[l][r] = True
            else: pass
            if dp[l][r] and (r - l + 1 > max_len):
                max_len = r - l + 1
                res_l = l
                res_r = r
    for l in range(len(s)-1, -1, -1):
        for r in range(l+2, len(s)):
            dp[l][r] = dp[l+1][r-1] and s[l]==s[r]
            if dp[l][r] and (r - l + 1 > max_len):
                max_len = r - l + 1
                res_l = l
                res_r = r
    return s[res_l:res_r+1]


print(longestPalindrome("cbabc"))   


            

 
