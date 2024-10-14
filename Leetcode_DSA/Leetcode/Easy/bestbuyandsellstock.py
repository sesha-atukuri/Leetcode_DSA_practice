def buy_sell_stock(prices):
    min_price = float('inf')
    max_profit =0
    for price in prices:
        if price<min_price:
            min_price = price
        profit = price - min_price
        if profit>max_profit:
            max_profit = profit
    return max_profit

print(buy_sell_stock([7,1,5,3,6,4]))