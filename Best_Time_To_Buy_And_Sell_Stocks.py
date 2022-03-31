#Best Time To Buy And Sell Stocks
#Problem Number-122
class Solution:
    def maxProfit(self, price: List[int]) -> int:
        mxpro=0
        for i in range(1,len(price)):
            if price[i]>price[i-1]:
                mxpro+=(price[i]-price[i-1])
        return mxpro
