class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            middle_value = matrix[middle // cols][middle % cols]

            if middle_value == target:
                return True
            elif middle_value > target:
                right = middle - 1
            elif middle_value < target:
                left = middle + 1
        return False