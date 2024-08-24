class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,min_length, current_sum = 0, 0, 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                if min_length == 0:
                    min_length = right - left + 1
                else:
                    min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length
