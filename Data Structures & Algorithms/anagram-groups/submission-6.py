class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord('a') - ord(c)] += 1

            ans[tuple(count)].append(s)
        return ans.values()    
