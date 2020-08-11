# 找出一个重复数
# 题干：
# 给出一个数组 nums 包含 n + 1 个整数，每个整数是从 1 到 n (包括边界)，
# 保证至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

# 要求：
# 1.不能修改数组(假设数组只能读)
# 2.只能用额外的O(1)的空间
# 3.时间复杂度小于O(n^2)
# 4.数组中只有一个重复的数，但可能重复超过一次


arr = [5,5,4,3,2,1]

def Count(nums, start, mid, end):
    res = 0
    for i in range(len(nums)):
        if nums[i] in range(start, mid+1):
            res += 1 
    return res

def findDuplicate(nums):
    start = 1
    end = len(nums) - 1
    if start == end:
        return start

    while start <= end:
        mid = (start + end) // 2
        res1 = Count(nums, start, mid, end)

        if start == end:
            if res1 > 1 :
                return start
            else:
                break

        if res1 > (mid - start + 1):
            end = mid
        else:
            start = mid + 1


print(findDuplicate(arr))
### 通过率 81%  超时了

