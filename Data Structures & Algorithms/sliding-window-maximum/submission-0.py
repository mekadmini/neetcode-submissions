class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        current_maxes = []
        while r < len(nums):
            current_maxes.append(max(nums[l:r+1]))
            l +=1
            r += 1
        return current_maxes

        