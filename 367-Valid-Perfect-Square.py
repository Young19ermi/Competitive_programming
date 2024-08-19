class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if sqrt(num) == int(sqrt(num)) else False