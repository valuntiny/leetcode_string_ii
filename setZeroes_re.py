'''
Quest:
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

    Example 1:
    Input:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

    Example 2:
    Input:
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output:
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

    Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Solution:
    use the first column and row as index
    but keep in mind that you need a special flag to let you know whether the first col originally contains 0 or not
'''


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zero = False
        row_zero = False

        if not matrix:
            return None

        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(m-1, 0, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0


test = Solution()
x = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
test.setZeroes(x)
print(x)