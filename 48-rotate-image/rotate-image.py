class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        