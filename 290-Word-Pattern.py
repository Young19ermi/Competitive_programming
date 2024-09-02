#this is the solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        check = defaultdict(list)
        l = list(pattern)
        k = list(s.split())
        if len(set(l)) != len(set(k)):
            return False
        if len(l) != len(k):
            return False
        for i in range(len(l)):
            check[l[i]].append(k[i])
        
        for key,items in check.items():
            if len(set(items)) > 1:
                return False
        return True 
