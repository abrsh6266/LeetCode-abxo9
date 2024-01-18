class Solution(object):
    def maxProfit(self, prices):
        profits = []
        cp = 10000
        sp = 0
        
        for price in prices:
            if price < cp:
                profits.append(sp-cp)
                cp = price 
                sp = 0
            if price > sp:
                sp = price

        profits.append(sp-cp)
        return max(profits)
    