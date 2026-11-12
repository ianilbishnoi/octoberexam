class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return [mid // cols, mid % cols]
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]
