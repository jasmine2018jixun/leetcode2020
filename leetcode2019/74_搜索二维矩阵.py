# coding utf-8 ************
import numpy as np 

m = [[]]
target = 11


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # 矩阵为空 m = []
    if not matrix:
        return False

    m = matrix
    i = 0
    # 矩阵的第一行为空 m = [[]]
    j = len(m[0]) - 1
    if j < 0:
        return False
    if m[i][j] == target:
        return True
    while i <= len(m) - 1 and j >= 0:
        if m[i][j] > target:
            j -= 1
        elif m[i][j] == target:
            return True
        else:
            i += 1
    return False
    


print(searchMatrix(m, target))
