"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = prices[0]
        
        max_profit = 0
        
        # loop through all the prices
        for price in prices:
            
            # calculate the currect profit with the min_price found by now
            profit = price - min_price
            
            # if current profit higher than current max profit, set current profit to max 
            if profit > max_profit:
                max_profit = profit
            
            # if the price found is < than min_price, set currect price to min
            if price <= min_price:
                min_price = price
        return max_profit
        
        
        
prices1 = [7,1,5,3,6,4]

prices2 = [7,6,4,3,1]

prices3 = [1]

prices4 = [9, 5, 4, 6, 2, 3]

prices5 = [1, 2]

print(Solution().maxProfit(prices1))



