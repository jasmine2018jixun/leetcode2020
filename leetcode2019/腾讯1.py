#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
def beat(n, m, list_c, list_w):
    res = 0
    list_c1 = []
    list_w1 = []
    for i in range(n):
        if list_c[i]/list_w[i] < m:
            list_c1.append(list_c[i])
            list_w1.append(list_w[i])
    length = len(list_c1)
    for i in range(length):
        res += list_w1[i]- list_c1[i]/m 
    return int(res)
    
        
    

if __name__ == "__main__":
    # 读取第一行的n和m
    line1 = sys.stdin.readline().strip()
    values = list(map(int, line1.split()))
    n, m = values[0], values[1]
    list_c = []
    list_w = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        c, w = values[0], values[1]
        list_c.append(c)
        list_w.append(w)
    print(beat(n, m, list_c, list_w))