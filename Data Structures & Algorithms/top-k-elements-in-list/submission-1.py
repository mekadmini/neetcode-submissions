class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1
            
        return [key for key, v in sorted(counts.items(), key=lambda item: -item[1])][:k]
        

        