# 1.选择排序
def search_sort(nums):
    for i in range(len(nums)-1):
        left = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[left]:
                left = j
        if left != i:
            nums[left], nums[i] = nums[i], nums[left]
    return nums

# 2.冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)-i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            if i == j:
                break
    return nums

        





# 简易对数器
import random

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def check(Int):
    i = 0
    flag = 'correct'
    while i < Int:
        nums = random_int_list(1,1000, 20)
        if sorted(nums) == bubble_sort(nums):
            i += 1
        else:
            flag = 'error'

    return flag

print(check(1000))

