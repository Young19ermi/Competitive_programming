def domino_piling(M, N):
    assert 1 <= M <= N <= 16, "The values of M and N should conform to the constraints: 1 <= M <= N <= 16"
    total_sqr=M*N
    output=total_sqr//2
    return output

M, N = map(int, input().split())
print(domino_piling(M, N))
