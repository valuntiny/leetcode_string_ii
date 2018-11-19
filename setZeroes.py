'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        flag_row = []
        flag_column = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    flag_row.append(i)
                    flag_column.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in flag_row or j in flag_column:
                    matrix[i][j] = 0