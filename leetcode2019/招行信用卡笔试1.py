#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def check(string1):
    if not string1: return 'NO'
    left = 0
    right = len(string1)-1
    while left <= right:
        if string1[left] == '1' and string1[right] != '1': 
            return 'NO'
        elif string1[left] == '2' and string1[right] != '5': 
            return 'NO'
        elif string1[left] == '3' and string1[right] != '8': 
            return 'NO'
        elif string1[left] == '4' and string1[right] != '7': 
            return 'NO'
        elif string1[left] == '6' and string1[right] != '9': 
            return 'NO'
        elif string1[left] == '5' and string1[right] != '2': 
            return 'NO'
        elif string1[left] == '8' and string1[right] != '3': 
            return 'NO'
        elif string1[left] == '7' and string1[right] != '4': 
            return 'NO'
        elif string1[left] == '9' and string1[right] != '6': 
            return 'NO'
        else:
            left += 1
            right -= 1
    return 'YES'
        
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        lines.append(line)
    for l in lines:
        print(check(l))