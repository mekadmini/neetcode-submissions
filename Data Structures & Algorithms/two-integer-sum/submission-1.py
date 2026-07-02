class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rests = {}
        for i in range(len(nums)):
            if target - nums[i] in rests.keys(): # if the complement is there 
                return [rests[target - nums[i]], i]
            rests[nums[i]] = i
        