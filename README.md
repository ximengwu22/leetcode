# LeetCode

## 股票问题
121.	Best Time to Buy and Sell Stock (Easy)
一次交易，找最大收益
```python3
for i in prices:
    low = min(low, i)
    profit = max(profit, i-low)
```

122.	Best Time to Buy and Sell Stock II (Easy)
可多次交易，找总最大收益
```python3
for i in range(1,len(prices):
    profit+=prices[i]-prices[i-1] if prices[i]-prices[i-1]>0
```

123.  Best Time to Buy and Sell Stock III (Hard)
最多两次交易（同理固定次数的多次），这种方法比较合理且避免了DP(好吧其实我不是很会DP)
```python3
for i in prices:
    buy1 = min(buy1, i) #找当前最低一次买入价格
    prof1 = max(prof1, i-buy1) #找第一次交易最大收益
    buy2 = min(buy2, i-prof1) #找用第一次收益购买的股票仍需付的最低价格
    prof2 = max(prof2, i-buy2) #两次交易总最大收益
return prof2
```

188.  Best Time to Buy and Sell Stock IV (Hard)
嗷嗷还是逃不过变量k次交易，上面的tricky tip就不能用了，不得不用DP的情况
```python3

```

714.	Best Time to Buy and Sell Stock with Transaction Fee (Med)
贪心，将交易费用考虑进买入价格中
```python3
for i in prices:
    if i < low:
        low = i
    elif i > low + fee:
        prof += i - low - fee
        low = i - fee #每次选择售出获利时，将下一次买入价格考虑为“不售出当前股票时”的情况，退还手续费，供后续对比使用
return prof
```

901.	Online Stock Span (Med)
每次都循环查找会造成o(n^2)超时，需要每次调用时适当合并前面的值，做存储
```
def next(self, price: int) -> int:
    cnt = 0
    #每次找与插入值最接近的值，倒序查找
    while self.stock and self.stock[-1][0] >= price:
        cnt += self.stock.pop[1]
    self.stock.append((price,cnt))
```

## 小偷问题
198	House Robber (Easy)

213	House Robber II (Med)

337	House Robber III (Med)




