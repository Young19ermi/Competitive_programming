testcase = int(input())
for _ in range(testcase):
    length = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-1]-nums[0])
    #print(max(nums)-min(nums))

