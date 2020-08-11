def myAtoi(str: str) -> int:
    if not str: return 0
    if str.startswith('+-') or str.startswith('-+') : return 0
    sign = 1
    temp = []
    flag = 0
    for s in str:
        if s == ' ' and flag == 0: 
            continue
        if s == '-' and flag == 0:
            sign = -1
            flag = 1
            continue
        if s == '+' and flag == 0:
            flag = 1
            continue
        temp.append(s)
        flag = 1
    digit = ['1','2','3','4','5','6','7','8','9','0']
    if not temp: return 0
    if temp[0] not in digit: return 0
    res = []
    for i in temp:
        if i in digit: 
            res.append(i)
        else:
            break
    if res[0] not in digit: return 0
    res = sum([int(res[i])*10**(len(res)-1-i) for i in range(len(res))])
    if sign == -1: res = -res
    if res>= -2**31 and res <= 2**31-1: return res
    elif res< -2**31: return -2**31
    else:return 2**31-1


print(myAtoi("   -42"))