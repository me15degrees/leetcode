class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        return 2 * sum(numbers) - sum(nums)
