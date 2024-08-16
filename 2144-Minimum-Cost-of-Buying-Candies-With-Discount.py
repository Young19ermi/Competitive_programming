class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        nums = list(reversed(sorted(cost)))
        s,c = 0,0
        flag = True
        for i in range(len(nums)):
            if c == 0:
                flag = True
            if c == 2:
                flag = False
                c = 0
            if flag:
                s += nums[i]
                c += 1
        return s