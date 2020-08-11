def merge_sort(alist):
    res = []
    if len(alist)<= 1:
        res.append(alist)
    elif len(alist) == 2:
        if alist[0] <= alist[1]:
            res = alist
        else:
            res = alist[::-1]
    else:
        mid = len(alist) // 2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                res.append(left[left_index])
                left_index += 1
            else:
                res.append(right[right_index])
                right_index += 1

        if left_index == len(left):
            res += right[right_index:]
        else:
            res += left[left_index:]
    print(res)
    return res

print(merge_sort([3,4,1,6,7,2,5,9]))


        

