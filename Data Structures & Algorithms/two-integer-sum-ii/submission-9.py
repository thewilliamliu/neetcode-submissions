class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        mp = {}

        for i in range(len(numbers)):
            if target - numbers[i] in mp:
                return [mp[target - numbers[i]] + 1, i + 1]
            else:
                mp[numbers[i]] = i