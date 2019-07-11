'''
A ring is compose of n circles as shown in diagram. Put natural number 1, 2, ..., n into each circle separately,
and the sum of numbers in two adjacent circles should be a prime.
Note: the number of first circle should always be 1. n (0 < n < 20).


Sample Input
6
8

Sample Output
Case 1:
1 4 3 2 5 6
1 6 5 2 3 4

Case 2:
1 2 3 8 5 6 7 4
1 2 5 8 3 4 7 6
1 4 7 6 5 8 3 2
1 6 7 4 3 8 5 2
'''
A = [None for i in range(0, 10)]
N = 6

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def dfs(cur):
    if cur == N:
        if is_prime(A[0]+A[N-1]):
            print(A[:N])
    else:
        for i in range(1, N+1):
            if i not in A[:cur]:
                if cur == 0 or is_prime(i+A[cur-1]):
                    A[cur] = i
                    dfs(cur+1)

dfs(0)








