#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def findk(nums, k, x):
    raw = nums.copy()
    left = 0
    right = len(raw)-1
    index = []
    while len(raw) > k:
        if abs(x - raw[0]) < abs(raw[-1] - x):
            if raw[-1] in raw[:-1]:
                index.append(raw.index(raw[-1]))
                raw.pop(raw.index(raw[-1]))
            else:
                raw.pop()
                index.append(right)
            right -= 1
        elif abs(x - nums[0]) == abs(nums[-1] - x):
             if nums[0] <= x:
                 if raw[-1] in raw[:-1]:
                     index.append(raw.index(raw[-1]))
                     raw.pop(raw.index(raw[-1]))
                 else:
                     raw.pop()
                     index.append(right)
                 right -= 1
             else:
                 if 
                 raw.pop(0)
                 index.append(left)
                 left += 1
        else:
            raw.pop(0)
            index.append(left)
            left += 1
    res = sum([abs(num - x) for num in raw])
    nnn = []
    for i in range(len(nums)):
        if i in index:
            nnn.append(nums[i])
        else:
            nnn.append(x)
    # print(x, 'index', index, 'nnn', nnn)
    return  res, nnn

def compare(nums1, nums2):
    for i in range(0, len(nums1)):
        if nums1[i] < nums2[i]: return nums1
        elif nums1[i] > nums2[i]: return nums2
        else: continue
    return nums1

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    n, k = line1.split()
    n = int(n)
    k = int(k)
    line2 = sys.stdin.readline().strip()
    nums = [int(i) for i in line2]
    # nums.sort()
    res_lucky = 9999999999999999
    res_nums = []
    for x in set(nums):
        temp_lucky, temp_nums = findk(nums, k, x)
        if temp_lucky < res_lucky:
            res_lucky = temp_lucky
            res_nums = temp_nums
        elif temp_lucky == res_lucky:
            res_nums = compare(res_nums, temp_nums)
    print(res_lucky)

    print(''.join([ str(r) for r in res_nums]))

     
        