import math

def maxSetSize(riceBags: list):
    riceBags.sort()
    
    # dp[i] the max set size when size = i
    dp = {}
    for num in riceBags:
        dp[num] = 1
    
    res = 0
    for n in riceBags:
        sqrt = int(math.sqrt(n))
        if sqrt**2 == n:
            dp[n] += dp.get(sqrt, 0)
            res = max(res, dp[n])
    print(dp)
    return res if res > 1 else -1

print(maxSetSize([625, 4, 2, 5, 25]))
print(maxSetSize([3, 9, 4, 2, 16]))