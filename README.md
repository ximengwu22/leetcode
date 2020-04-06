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
```
for i in range(1,len(prices):
    profit+=prices[i]-prices[i-1] if prices[i]-prices[i-1]>0
```

123.  Best Time to Buy and Sell Stock III (Hard)
最多两次交易（同理多次）
```
for i in prices:
    buy1 = min(buy1, i) #找当前最低一次买入价格
    prof1 = max(prof1, i-buy1) #找第一次交易最大收益
    buy2 = min(buy2, i-prof1) #找用第一次收益购买的股票仍需付的最低价格
    prof2 = max(prof2, i-buy2) #两次交易总最大收益
return prof2
```

188.  Best Time to Buy and Sell Stock IV (Hard)

714.	Best Time to Buy and Sell Stock with Transaction Fee (Med)

901.	Online Stock Span (Med)


## 小偷问题
198	House Robber (Easy)

213	House Robber II (Med)

337	House Robber III (Med)




