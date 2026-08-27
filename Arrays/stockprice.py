class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        present=0
        minprice=prices[0]

        for price in prices:
            if(price < minprice):
                minprice=price
            else:
                present=price-minprice
                if(present>profit):
                    profit=present
            
        return profit
        
        
     #brute force approach (down)
     
     class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        present=0
        for i in range(len(prices)-1):
      
            for j in range(i+1,len(prices)):
                present=prices[j]-prices[i]
                if(present>profit):
                    profit=present


        return profit