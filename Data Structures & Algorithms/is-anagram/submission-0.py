class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {} # dict with 26 letters so const O(1)!!!
        # now O(n) just save the appearances of letters
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        # now O(m) 
        for letter in t:
            if letter not in letters:
                return False # we found an extra letter in t not found in s
            if letters[letter] == 1:
                del letters[letter] # pop the last one, if there is more in t we know later it is False
                continue
            letters[letter] -= 1
        
        return letters == {}
            
        