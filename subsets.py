from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_list = []
        self.depth_first_search(0, nums, [], subsets_list)
        return subsets_list

    def depth_first_search(self, start_index: int, nums: List[int], current_path: List[int], subsets_list: List[List[int]]):
        subsets_list.append(current_path[:])

        for i in range(start_index, len(nums)):
            self.depth_first_search(i + 1, nums, current_path + [nums[i]], subsets_list)