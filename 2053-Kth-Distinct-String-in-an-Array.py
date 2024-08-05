class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        nums = []
        for n in arr:
            if arr.count(n) == 1:
                nums.append(n)
        print(nums)

        if k-1 in range(0,len(nums)):
            return nums[k-1]
        else:
            return ""