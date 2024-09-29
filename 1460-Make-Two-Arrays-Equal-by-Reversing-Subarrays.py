class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for n in arr:
            if n not in target:
                return False
            if arr.count(n) != target.count(n):
                #solution
                return False
        return True
