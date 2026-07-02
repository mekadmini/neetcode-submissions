class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_letters = {}
        start_index = 0
        end_index = 0
        longest_string_size = 0

        while end_index < len(s) and start_index <= end_index:
            for i in range(start_index, end_index + 1):
                if s[i] in seen_letters and i != seen_letters[s[i]] and seen_letters[s[i]] >= start_index:
                    start_index = seen_letters[s[i]] + 1
                seen_letters[s[i]] = i
            longest_string_size = max(longest_string_size, end_index - start_index + 1)
            end_index += 1    
            

        return longest_string_size   


        