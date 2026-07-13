class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pair = []
        #for i in range(len(position)):
        #    pair.append((position[i], speed[i]))
        
        #pair = [(p,s) for p,s in zip(position,speed)]
        pair = [(p,speed[i]) for i,p in enumerate(position)]
        
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        