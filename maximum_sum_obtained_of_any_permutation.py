class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lst = [0]*len(nums)

        for request in requests:
            lst[request[0]] += 1
            if request[1] != len(nums)-1:
                lst[request[1]+1] -= 1
        accumulate = 0
        for i in range(len(lst)):
            accumulate += lst[i]
            lst[i] = accumulate

        lst.sort(reverse=True)
        nums.sort(reverse=True)
        rst = 0
        
        for i in range(len(lst)):
            if lst[i] == 0:
                break
            rst += nums[i]*lst[i]

        return rst%(10**9+7)
