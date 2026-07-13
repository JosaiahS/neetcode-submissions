class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False

    # for loop: O(n) = Runtime: O(n)
    # set(): Worst case O(n). Memory: O(n)