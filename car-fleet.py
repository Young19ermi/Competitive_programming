class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        inds = list(range(n))
        inds.sort(key=lambda i: position[i], reverse=True)
        
        cur = inds[0]
        result = 1
        
        for i in range(1, n):
            idx = inds[i]
            if (target - position[idx]) * speed[cur] > (target - position[cur]) * speed[idx]:
                result += 1
                cur = idx
        
        return result
