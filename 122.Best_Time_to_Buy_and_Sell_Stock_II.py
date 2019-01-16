class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #记录当前最小值，如果遇到array[i]<min，那么加上当前的最大值；更新min。
        if prices == []: 
            return 0
        res = 0
        small = prices[0]
        for n in prices[1:]:
            if small < n: 
                res += n - small
                small = n
            else:
                small = min(n,small)
        return res

# Test
t = Solution()
print(t.maxProfit([7,1,5,3,6,4]))
print(t.maxProfit([1,2,3,4,5]))
print(t.maxProfit([7,6,4,3,1]))