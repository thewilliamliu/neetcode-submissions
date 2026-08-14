# Don't confuse key with the value.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            a = numbers[i]
            b = numbers[j]

            if a + b == target:
                return [i + 1, j + 1]

            if a + b > target:
                j -= 1
            
            if a + b < target:
                i += 1
        