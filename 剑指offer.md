# 剑指offer
- 😊基于python语言实现😺
- 建议先练习一些数据结构（链表、树、栈和队列、哈希表、字符串、数组与矩阵、图、位运算）以及算法思想（双指针、排序、贪心思想、二分查找、分治、搜索、动态规划、数学）相关的题，推荐follow https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E7%9B%AE%E5%BD%95.md
- 最后把剑指offer当做一个练兵场，进一步总结一些解题模板，重在吃透、多解法
---
## 3.数组中的重复数字
- 是否要求找出所有重复数字？
- 是否允许修改数组？
- 时、空复杂度的要求？\
<br/>https://leetcode.com/problems/find-the-duplicate-number/description/(找出一个重复数)<br/>
<br/>https://leetcode.com/problems/find-all-duplicates-in-an-array/description/（找出所有重复数）<br/>
<br/>https://www.lintcode.com/problem/find-the-duplicate-number/description（不允许修改数组）<br/>
#### 常用解法：
(1)排序后遍历，排序的时间复杂度至少为O(nlogn)；\
(2)哈希表，时间复杂度O(n)，空间复杂度O(n)；\
(3)利用数字和index的映射关系，每个数字最多只要交换2次就能找到自己的位置，时间复杂度O(n)，空间复杂度O(1),<修改了数组>；

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

(4)Cycle Detection


