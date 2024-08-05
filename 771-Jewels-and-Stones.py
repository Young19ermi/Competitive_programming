class Solution:
    def numJewelsInStones(self, num1: str, num2: str) -> int:
        
        count = 0 
        for n in num2:
            if n in num1:
                count += 1
        return count