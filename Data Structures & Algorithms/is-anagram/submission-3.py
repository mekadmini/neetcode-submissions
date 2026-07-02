class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        # O(n)
        for i in s:
            if i in letters.keys():
                letters[i] +=  1
            else:
                letters[i] = 1
        
        # O(m)
        for i in t:
            if i not in letters.keys():
                return False
            letters[i] -= 1
            if letters[i] == 0:
                del letters[i]
        return letters == {}
            
        