class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            key = "".join(sorted(word)) ## Sorted returns a list, must join together like this.
            if key not in groups: ## Making a list of lists.
                groups[key] = [] 
            groups[key].append(word) 

        return list(groups.values()) 