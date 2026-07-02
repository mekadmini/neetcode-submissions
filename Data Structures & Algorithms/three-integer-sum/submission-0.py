class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_dict = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    entry_sum = nums[i] + nums[j]
                    if entry_sum in sum_dict.keys():
                        sum_dict[entry_sum] += [(i,j)]
                    else:
                        sum_dict[entry_sum] =[(i,j)]
        print(sum_dict)
        output = set()
        for k in range(len(nums)):
            if -nums[k] in sum_dict.keys():
                candidates = sum_dict[-nums[k]]
                for candidate in candidates:
                    if k == candidate[0] or k == candidate[1]:
                        continue
                    ls = sorted([nums[k], nums[candidate[0]], nums[candidate[1]]])
                    output.add((ls[0], ls[1], ls[2]))
        return list(output)


        