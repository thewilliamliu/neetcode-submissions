class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_without_first = nums[1:]
        nums_without_last = nums[:-1]
    
        return max(self.robHelper(nums_without_first), self.robHelper(nums_without_last))
        

    def robHelper(self, nums):
        profit = [0] * len(nums)
        
        for i, cash in enumerate(nums):
            if i == 0:
                profit[i] = nums[0]
            elif i == 1:
                profit[i] = max(nums[0], nums[1])
            else:
                profit[i] = max(profit[i-1], profit[i-2] + nums[i])
        
        return profit[len(nums) - 1]