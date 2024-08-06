class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def dfs(start, sub):
            if len(sub) != len(set(sub)):
                return
            nonlocal max_len
            max_len = max(max_len, len(sub))
            for i in range(start, len(arr)):
                dfs(i + 1, sub + arr[i])

        max_len = 0
        dfs(0, "")
        return max_len
