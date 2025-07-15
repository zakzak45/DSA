def MaximumP(prices):
   if not prices:
      return 0
   
   min_price =float("inf")
   max_profit=0

   for price in prices:
      min_price =min(price,min_price)
      max_profit=(max_profit,price-min_price)

   return max_profit
#solid logic for the best time to sell and but problem 