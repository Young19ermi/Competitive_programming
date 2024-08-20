class Solution:
    numbers = {
        6: True, 
        28: True, 
        496: True, 
        8128: True, 
        33550336: True, 
        8589869056: True, 
        137438691328: True, 
        2305843008139952128: True, 
        2658455991569831744654692615953842176: True,
        191561942608236107294793378084303638130997321548169216: True
    }
    def checkPerfectNumber(self, num: int) -> bool:
        return num in self.numbers
        
        