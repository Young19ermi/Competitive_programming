a = int(input())
for i in range(a):
    b = int(input())
    arr = list(map(int , input().split()))
    arr.sort()
    for j in range(b - 1):
        if arr[j + 1] - arr[j] > 1:
            print("NO")
            break
    else:
        print("YES")
