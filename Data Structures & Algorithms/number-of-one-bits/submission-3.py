# Bitwise AND uses & symbol. 
# Any of those symbols automatically work in bit representation.

# Use len(str(n)) to get length of string representation, 
# n.bit_length() to get binary length.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(n.bit_length()):
            if 1 << i & n != 0:
                count += 1

        return count

        
        