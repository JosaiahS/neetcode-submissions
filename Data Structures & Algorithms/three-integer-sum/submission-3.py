class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, current in enumerate(nums):

            if current > 0:
                break

            if i > 0 and current == nums[i - 1]:
                continue

            l,r = i + 1, len(nums) - 1

            while l < r:
                triplet = current + nums[l] + nums[r]

                if triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    res.append([current, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res