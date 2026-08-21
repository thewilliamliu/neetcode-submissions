class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_length = 0
        freq = {}
        max_freq = 0
        
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            length = r - l + 1
            replacements = length - max_freq
            
            while replacements > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1
                length = r - l + 1
                replacements = length - max_freq

            max_length = max(max_length, r - l + 1)

            r += 1

        return max_length

        