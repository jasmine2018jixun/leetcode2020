#剑指offer 类似题
# 有两个排序的数组 A1 和 A2， 内存在 A1 的末尾有足够多的空余空间容纳 A2.
# 请实现一个函数，把 A2中的所有数字插入 A1 中，并且所有数字是有序的
arr1 = [3, 4, 7, 9, 10]
arr2 = [1, 2, 4, 5]

res = arr1 + arr2
print(res)
p1 = len(arr1) - 1
p2 = len(arr2) - 1
i = len(res) - 1
while p1 > 0 and p2 > 0 :
    if arr1[p1] == arr2[p2]:
        res[i] = arr1[p1]
        i -= 1
        res[i] = arr2[p2]
        i -= 1
        p1 -= 1
        p2 -= 1
    elif arr1[p1] > arr2[p2]:
        res[i] = arr1[p1]
        i -= 1
        p1 -= 1
    else:
        res[i] = arr2[p2]
        i -= 1
        p2 -= 1

while p1 != -1:
    res[i] = arr1[p1]
    p1 -= 1
    i -= 1
while p2 != -1:
    res[i] = arr2[p2]
    p2 -= 1
    i -= 1

print(res)

    
    