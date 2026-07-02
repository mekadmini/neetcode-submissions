class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(key=lambda x:-x)
            if stones[0] == stones[1]:
                stones = stones[2:]
                continue
            stones = [stones[0] - stones[1]] + stones[2:]
        
        if stones == []:
            return 0
        return stones[0]
        
        