class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
        return -1