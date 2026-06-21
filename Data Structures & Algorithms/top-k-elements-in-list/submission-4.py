from collections import Counter
## Counter is an incredibly useful class. Returns (value, frequency) symbol table.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        ## Use .items() on a map to get pairs and .values() to just get values.
        ## Commas separate the sort statements here.
        ## Lambda is like a function inside (e.g. lambda input: output)
        sorted_freq = sorted(freq.items(), key = lambda freq: freq[1], reverse = True)
        
        ## Use [] to declare arrays, and {} to declare maps.
        output = []

        for i in range(k):
            output.append(sorted_freq[i][0])

        return output

            
            

        