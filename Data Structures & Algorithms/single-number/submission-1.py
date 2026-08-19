# XOR is communitive, a ^ a = 0.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]

        if len(nums) == 1: return result

        for number in nums[1:]:
            result = result ^ number

        return result

        
            
            
        