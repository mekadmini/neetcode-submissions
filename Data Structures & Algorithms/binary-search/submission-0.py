class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
        if nums[l] == target:
            return l
        return -1
        