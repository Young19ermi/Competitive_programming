class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        target = [0]*26
        window = [0]*26

        for i in range(n):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        for i in range(n, m):
            if window == target:
                return True
            window[ord(s2[i-n]) - ord("a")] -= 1
            window[ord(s2[i]) - ord("a")] += 1
            
        return window == target
