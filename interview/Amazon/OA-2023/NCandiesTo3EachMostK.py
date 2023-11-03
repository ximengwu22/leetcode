def numRollsToTarget(n: int, k: int, target: int) -> int:
    # sum(n) = sum[n-1]+[1..k] == target
    # dp[n][target]: # of ways with n dice for target
    # dp[n][target] = sum(dp[n-1][target-(1...k)])
    # dp[1][1...k] = 1
    # dp[2][2] = sum(dp[1][1])
    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    for j in range(min(k, target)+1):
        dp[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(1, target + 1):
            for dn in range(1, k+1):
                if 0 < j - dn:
                    dp[i][j] += dp[i-1][j-dn]
        # print(dp[i])
    
    return dp[n][target]%(10**9+7)

# print(numRollsToTarget(1, 6, 3))
# print(numRollsToTarget(2, 6, 7))
# print(numRollsToTarget(30, 30, 500))


# Followup Question 2:
# Count the number of ways to distribute toy cars among 3 children such that each child should not have more than K toy cars, and total number of distributed toy cars equals S.
# Constraints :
# 2 <= k <= 5 * 10^3
# 0<= s <= 3*k

def followup2(k: int, s: int):
    dp = [[0 for _ in range(s+1)] for _ in range(4)]
    for j in range(min(s, k)+1):
        dp[1][j] = 1
    # print(dp[0])
    for i in range(2, 4):
        for j in range(s+1):
            for dk in range(k+1):
                if j-dk >= 0:
                    dp[i][j] += dp[i-1][j-dk]
        # print(dp[i])
    
    return dp[3][s]

print(followup2(2, 2))
print(followup2(5, 15))