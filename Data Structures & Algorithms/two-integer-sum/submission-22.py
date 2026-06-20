class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        ## Range and enumerate are the two ways to deal with a for loop.
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i 

        return []