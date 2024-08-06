class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, subArray):
            if len(subArray) >= 2:
                results.add(tuple(subArray))  # Use a set to store results
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if not subArray or nums[i] >= subArray[-1]:
                    dfs(i + 1, subArray + [nums[i]])

        results = set()
        dfs(0, [])

        return [list(sub) for sub in results]
