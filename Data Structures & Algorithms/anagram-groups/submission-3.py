from collections import defaultdict ## Makes empty list appear automatically.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word)) ## Sorted returns a list, must join together like this.
            groups[key].append(word) 

        return list(groups.values()) 
        