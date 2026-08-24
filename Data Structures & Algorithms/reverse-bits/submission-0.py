class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        num_bits = 32
        for i in range(num_bits):
            bit = (n >> i) & 1
            bit = bit<<(31-i)
            res+=bit
        
        return res