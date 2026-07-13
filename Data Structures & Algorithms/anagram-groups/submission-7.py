class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        
        for ss in strs:
            count = [0] * 26
            for s in ss:
                count[ord(s) - ord('a')] += 1
            anagram[tuple(count)].append(ss)
        return list(anagram.values())
                