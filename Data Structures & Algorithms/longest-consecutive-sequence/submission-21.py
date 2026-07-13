class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest= 1
        res=0
        cur = 0
        for i, num in enumerate(nums):
            cur = num
            if cur - 1 not in numset:
                longest = 1
                while cur + 1 in numset:
                    longest += 1
                    cur += 1
                res = max(longest, res)


        return res