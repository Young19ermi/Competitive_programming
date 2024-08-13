class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
    
        if len(nums) == 0:
            return 0
    
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                print(slow)
                print(fast)
                nums[slow] = nums[fast]
    
        return slow + 1
