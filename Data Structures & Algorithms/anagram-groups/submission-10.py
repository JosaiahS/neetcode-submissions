class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            dictionary[tuple(freq)].append(s)
        
        return list(dictionary.values())
                
