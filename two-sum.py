class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = dict()

        for idx, value in enumerate(nums):
            diff = target - value
            
            val = hashmap.get(diff)
            if val is not None:
                return [idx, val]
            
            hashmap[value] = idx
        
        return result