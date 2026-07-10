class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for x,y in enumerate(nums):
            indices[y] = x
        
        for x,y in enumerate(nums):
            s=target-y
            if s in indices and indices[s] != x:
                return [x, indices[s]]
        