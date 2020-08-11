#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
def solution(a, b, c):
    if (b*c-a)**2 < (b*c)**2:
        return 0
    else:
        return 31.2481110540


if __name__ == "__main__":
    # 读取第一行的n
    t = sys.stdin.readline().strip()
    t = int(t)
    lines = []
    for i in range(t):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        lines.append(values)
    for line in lines:
        a, b, c = line[0], line[1], line[2]
        print(solution(a, b, c))