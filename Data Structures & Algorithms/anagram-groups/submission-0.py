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
        # O(m + m)
        return letters == {}

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            found = False
            for k in anagrams.keys():
                if self.isAnagram(s,k):
                    anagrams[k] += [s]
                    found = True
                    break
            if not found:        
                anagrams[s] = [s]
        return list(anagrams.values())



        
        