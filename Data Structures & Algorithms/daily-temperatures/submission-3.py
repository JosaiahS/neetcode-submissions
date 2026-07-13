class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp : ind

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                tmp, ind = stack.pop()
                res[ind] = i - ind
            stack.append([temp, i])
        return res