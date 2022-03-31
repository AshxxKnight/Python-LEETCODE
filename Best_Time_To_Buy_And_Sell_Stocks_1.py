class Solution:
    def maxProfit(self, price: List[int]) -> int:
        lsf=float('inf')
        mxpro=0
        for i in range(0,len(price)):
            if price[i]<lsf:
                lsf=price[i]
            else:
                mxpro=max((price[i]-lsf),mxpro)
        return mxpro
