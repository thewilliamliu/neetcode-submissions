class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums.copy()
        
        for i, val in enumerate(nums):
            for j, val2 in enumerate(nums2):
                if val + val2 == target and i != j:
                    return [i, j]