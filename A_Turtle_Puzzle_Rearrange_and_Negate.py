testcase = int(input())
for _ in range(testcase):
    length = int(input())
    nums = list(map(int, input().split()))
    num = []
    for n in nums:
        num.append(abs(n))
    print(sum(num))