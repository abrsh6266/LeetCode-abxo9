class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1
        maxi = 0
        n = len(prices)
        while r < n:
            if prices[l]<prices[r]:
                maxi = max(maxi,prices[r]-prices[l])
            else:
                l = r
            r += 1
        return maxi