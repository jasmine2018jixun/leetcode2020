#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
import collections

def subarray(nums, m):
    count_mod = [0]
    for num in nums:
        count_mod.append((count_mod[-1] + num) % m)
    count = collections.Counter(count_mod)
    return int(sum((v-1)*v/2 for v in count.values()))
if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    n, m = line1.split()
    n = int(n)
    m = int(m)
    line2 = sys.stdin.readline().strip()
    nums = list(map(int, line2.split()))
    print(subarray(nums, m))