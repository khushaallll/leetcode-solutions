def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price > min_price:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        else:
            min_price = price
    
    return max_profit
prices = [7,6,4,3,1]
print(maxProfit(prices))
