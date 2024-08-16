class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)

        s = 0
        i = 0
        while i < len(nums):
            s += min(nums[i],nums[i+1])
            i += 2
        return s