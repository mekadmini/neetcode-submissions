class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        all_perms = []

        for n in nums:
            new_list = nums.copy()
            new_list.remove(n)
            perms = self.permute(new_list)
            all_perms += [[n] + l for l in perms]
            
        return all_perms
        

        