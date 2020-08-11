def maxArea(height) -> int:
    if len(height) < 2: return 
    if len(height) == 2: return min(height[0], height[1])
    left = 0
    right = len(height)-1
    res = (right-left) * min(height[left], height[right])

    while left < right:
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
        temp = (right-left) * min(height[left], height[right])

        if temp > res: res = temp
    return res

print(maxArea([1,2,1]))