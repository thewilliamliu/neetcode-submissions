class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        ## Instead of sorting, we can assign a frequency counter for each.

        groups = defaultdict(list)
        
        for word in strs:
            
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            ## Can't use a list (it is immutable) as an index. Change to tuple.
            groups[tuple(count)].append(word) 
        
    
        return list(groups.values()) ## Converts hash into a list.


        