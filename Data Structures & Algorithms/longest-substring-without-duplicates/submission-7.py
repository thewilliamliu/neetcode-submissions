class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        length = 0
        seen = set()
        
        while right < len(s):
            # Need to CONTINUE removing until all duplicates are gone.
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            right += 1

            length = max(right - left, length)

        return length
            


            
        