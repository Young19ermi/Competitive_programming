class KthLargest:  
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.k = k
        self.nums = nums
    def add(self, val: int) -> int:
        
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]