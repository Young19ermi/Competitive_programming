#here is the solution 
class Solution:
    def hammingWeight(self, n: int) -> int:
        k = list(str(bin(n)))
        return k.count('1')
r
