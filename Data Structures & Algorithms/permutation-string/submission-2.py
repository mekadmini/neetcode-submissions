class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        count = {}
        current = {}

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        for c in s2[l: r]:
            current[c] = 1 + current.get(c, 0)
        
        while r < len(s2):
            current[s2[r]] = 1 + current.get(s2[r], 0)
            if count == current:
                return True
            current[s2[l]] -= 1
            if current[s2[l]] == 0:
                current.pop(s2[l])
            r+=1
            l+=1
        return False
        