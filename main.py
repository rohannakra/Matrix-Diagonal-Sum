# https://leetcode.com/problems/matrix-diagonal-sum/

def diagonal_sum(mat):
    d_sum = 0
    indices = []

    for i in range(len(mat)):    # left diagonal
        d_sum += mat[i][i]
        indices.append([i, i])
    
    for i, j in zip(range(len(mat)), list(range(len(mat)))[::-1]):    # right diagonal
        if [i, j] in indices:
            continue
        else:
            d_sum += mat[i][j]
    
    return d_sum


print(diagonal_sum([[1,2,3],
              [4,5,6],
              [7,8,9]]))

print(diagonal_sum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))

print(diagonal_sum([[5]]))

# -----------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d_sum = 0
        indices = []

        for i in range(len(mat)):    # left diagonal
            d_sum += mat[i][i]
            indices.append([i, i])
    
        for i, j in zip(range(len(mat)), list(range(len(mat)))[::-1]):    # right diagonal
            if [i, j] in indices:
                continue
            else:
                d_sum += mat[i][j]
    
        return d_sum
