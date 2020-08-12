# 剑指offer
- 😊基于python语言实现😺
- 建议先练习一些数据结构（链表、树、栈和队列、哈希表、字符串、数组与矩阵、图、位运算）以及算法思想（双指针、排序、贪心思想、二分查找、分治、搜索、动态规划、数学）相关的题，推荐 Follow：
<br/>https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E7%9B%AE%E5%BD%95.md<br/>

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

(4)Cycle Detection\
相当于有环的链表找入环口。利用快、慢指针，快指针每次走2步，慢指针每次走1步，链表有环则快慢指针一定会相遇。假设起点到入环扣距离为a，入环口距离两指针相遇的点距离为b，环长为L，则有2（a+b) = a + b + kL,可得a = kL - b, 可见相遇后，将一指针从起点开始每次走1步，另一指针从相遇点开始每次走1步，则两指针会在入环口相遇。
利用快、慢指针

    def findDuplicate(self, nums: List[int]) -> int:
        h = t = nums[0]
        while True:
            h = nums[nums[h]]
            t = nums[t]
            if h == t:
                break
        pr1 = nums[0]
        pr2 = t 
        while pr1 != pr2:
            pr1 = nums[pr1]
            pr2 = nums[pr2]
        return pr1  
(5)二分查找+统计区间内数字的数量（But 不能确定每个数字各出现一次还是某个数字出现了2次）时间复杂度O(n)，空间复杂度O(n)\
把1-n的数字从中间的数字分为2部分，[1,m]区间内的为part1，[m+1,n]区间内的为part2，统计区间内数字的数量，超过区间的长度则一定包含重复数

    def findDuplicate(self, nums):
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left