class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l,r=0,0        
        for x in prices:
            while r<len(prices):                
                if prices[l]>prices[r]:
                    r+=1
                    continue
                else:
                    profit =max(profit,prices[r]-prices[l])
                    r+=1
            l+=1    
            r=l
        return profit
                    