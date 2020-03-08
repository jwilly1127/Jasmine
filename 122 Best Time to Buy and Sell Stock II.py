class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        valley = True
        profit = 0
        low_cost = float('inf')
        for day, price in enumerate(prices):
            if(valley):
                if(price > low_cost):
                    #We are ascending
                    peak = price
                    valley = False
                else:
                    #still in valley
                    low_cost = price
            else:
                if(price >= peak):
                    #still ascending
                    peak = price
                else:
                    #descending
                    profit += peak - low_cost
                    low_cost = price
                    valley = True
        
        if(not valley):
            profit += (peak - low_cost)
        
        return profit
                
                
            
        
