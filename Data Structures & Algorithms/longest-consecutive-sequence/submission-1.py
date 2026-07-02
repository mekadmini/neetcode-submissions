class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        start_dict = {}
        for num in nums:
            if num - 1 not in nums:
                start_dict[num] = 1
        
        for num in nums:
            if num not in start_dict.keys() and (num - 1) in start_dict.keys():
                current_count = start_dict[num - 1] + 1
                del start_dict[num - 1]
                start_dict[num] = current_count
        return max(start_dict.values())




        