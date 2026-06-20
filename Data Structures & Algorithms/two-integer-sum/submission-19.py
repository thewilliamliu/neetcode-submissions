class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = [] 

        ## Enumerate: list -> gives (index, value) for each element of list.
        for i, num in enumerate(nums):
            A.append([num, i])
            ## Position 0 holds value, position 1 holds index.

        A.sort() ## Sorts based on number, but retains index.

        i, j = 0, len(A) - 1 ## Sets pointers up.

        while i < j: ## Common two pointer method.
            current = A[i][0] + A[j][0]
            ## A[selects pair][selects 0 or 1]
        
            if current == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
                ## Returns smaller index first.

            elif current < target:
                i += 1
            
            elif current > target:
                j -= 1

        return []