class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
#optimized solution
        minimums = []
        res = float('inf')  
        
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])

            if diff < res:
                res = diff
                minimums = [[arr[i], arr[i + 1]]]
            elif diff == res:
                minimums.append([arr[i], arr[i + 1]])

        return minimums
