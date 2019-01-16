class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = 0
        pre = prices[0]
        for i in range(1, len(prices)):
            pre = min(pre, prices[i])   #前面的数字中最小的
            ans = max(prices[i] - pre, ans)
        return ans
        
# Test
t = Solution()
print(t.maxProfit([7,1,5,3,6,4]))
print(t.maxProfit([7,6,4,3,1]))