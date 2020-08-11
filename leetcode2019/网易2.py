def daguaishou(n, D, nums_a, nums_b):
    nums = zip(nums_a, nums_b)

    a, b = zip(*sorted(nums))
    a, b = list(a), list(b)
    res = 0
    for i in range(n):
        if D > a[i]:
            D += 1
        else:
            D -= a[i]
            res += a[i]

    return res


A = [1,2,3,4,5,6]
B = ['h','e','l','l','o',',']
print(daguaishou(1, A, B))