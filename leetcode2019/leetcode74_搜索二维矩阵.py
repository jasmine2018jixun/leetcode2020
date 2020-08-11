def searchMatrix(matrix, target: int):
    if not matrix: return False
    if not matrix[0]: return False
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False
    if target == matrix[0][0]: return True
    i = j = 0
    while i <= len(matrix)-1:
        if target <= matrix[i][-1]:
            if target in matrix[i]:
                return True
            else: return False
        else:
            i += 1
    return False



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(searchMatrix(matrix, 4))
