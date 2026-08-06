class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for c in sandwiches:
            if cnt[c] > 0:
                cnt[c] -= 1
                res -= 1
            else:
                return res
        
        return res