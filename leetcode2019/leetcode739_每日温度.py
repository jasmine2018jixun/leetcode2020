def cal(T):
    ans = []
    for l in range(len(T)-1):
        r = l + 1
        while r < len(T) and T[r]<= T[l]:
            r += 1
        if r < len(T):
            ans.append(r-l)
        else:
            ans.append(0)


    ans.append(0)
    return ans

print(cal([73, 74, 75, 71, 69, 72, 76, 73]))
