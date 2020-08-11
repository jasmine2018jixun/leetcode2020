#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    n = int(n)
    # 读取N个物品的价格
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line.split()))
    nums.sort()
    nums = nums[::-1]
    res = [nums[i-1] for i in range(1, len(nums)) if i % 3 == 0]
    print(sum(nums)-sum(res))
        
   