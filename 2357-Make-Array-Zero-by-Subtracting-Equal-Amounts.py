class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       
     
        def callme(nums,count):
            
            while 0 in nums:
                nums.remove(0)
            
            if nums == []:
                return count

            mini = min(nums)
          
            for i in range(len(nums)):
                nums[i] -= mini
            
            if list(set(nums)) == 1 and nums[0] == 0:
                return 
            else:
                
                return callme(nums,count+1)
        return callme(nums,0)