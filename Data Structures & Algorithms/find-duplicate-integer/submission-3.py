class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == start:
                return start
            start = nums[i]
        return start
        