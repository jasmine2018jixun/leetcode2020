#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
def solution(m,n):
    if n == 1:
        return 0
    elif n == 2:
        if m == 1: return 1
        else:return m
    else:
        return (m**n-m*((m-1)**(2*(n-2))))%100003 # 快速幂取模

if __name__ == "__main__":
    # 读取第一行的n和m
    line1 = sys.stdin.readline().strip()
    values = list(map(int, line1.split()))
    m, n = values[0], values[1]
    print(solution(m,n))