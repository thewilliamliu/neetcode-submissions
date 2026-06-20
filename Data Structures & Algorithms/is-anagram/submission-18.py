from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = Counter(s), Counter(t)

        if countS == countT:
            return True

        return False

        
