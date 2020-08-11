def hcf(x):
    '''查找数组的最大公约数'''                                #计算最大公约数
    smaller=min(x)
    for i in reversed(range(1,smaller+1)):
        if list(filter(lambda j: j%i!=0,x)) == []:
            return i

def find(num, nums):
    if num < 2: return -1
    diff = []
    for i in range(0, num-1):
        diff.append(nums[i+1]-nums[i])
    if hcf(diff): return hcf(diff)
    else: return -1

print(find(4, [1, 2, 1, 1]))
