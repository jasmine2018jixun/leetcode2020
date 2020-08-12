# 剑指offer
- 😊基于python语言实现😺
---
## 3.数组中的重复数字
- 是否要求找出所有重复数字？
- 是否允许修改数组？
- 时、空复杂度的要求？\
  https://leetcode.com/problems/find-the-duplicate-number/description/(找出一个重复数）\
  https://leetcode.com/problems/find-all-duplicates-in-an-array/description/（找出所有重复数）\
  https://www.lintcode.com/problem/find-the-duplicate-number/description（不允许修改数组）
#### 常用解法：
(1)排序后遍历，排序的时间复杂度至少为O(nlogn)；\
(2)哈希表，时、空复杂度O(n)；\
(3)利用数字和index的映射关系，每个数字最多只要交换2次就能找到自己的位置，时间复杂度O(n)，空间复杂度O(1)；

    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
            else:
                while nums[i] != i:
                    if nums[nums[i]] == nums[i]:
                        return nums[i]
                    else:
                        t = nums[i]
                        nums[i], nums[t] = nums[t], nums[i]

(4)


