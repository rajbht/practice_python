from icecream import ic

def maxProfit(prices):

    buy = min(prices)
    start = prices.index(buy)
    sell = 0
    for i in range(start,len(prices)):
        if prices[i] > sell:
            sell = prices[i]
            
    return sell - buy


def maxProfit1(prices):

    maxP = 0
    minP = prices[0]
    for price in prices[1:]:
        maxP = max(maxP, price - minP)
        minP = min(minP, price)
    return maxP



ic(maxProfit([7,6,4,3,1]))
ic(maxProfit([7,1,5,3,6,4]))

ic(maxProfit1([7,6,4,3,1]))
ic(maxProfit1([7,1,5,3,6,4]))

# maxP=0
# i=1
# price=1
# maxP = max(0,1-7) = 0
# minP = min(7,1) = 1

# i=2
# price=5
# maxP = max(0,5-1) = 4
# minP = min(1,5) = 1

# i=3
# price=3
# maxP = max(4,3-1) = 4
# minP = min(1,3) = 1

# i=4
# price=6
# maxP = max(4,6-1) = 5
# minP = min(1,6) = 1

# i=5
# price=4
# maxP = max(5,4-1) = 5
# minP = min(1,4) = 1