class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = float("-inf")
        l = 0
        duplicate = set()
        for r in range(len(s)):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                l += 1
            duplicate.add(s[r])
            res = max(res, r-l+1)
        return res