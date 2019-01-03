class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #就是斐波那契数列
        if n <= 1:
            return 1
        pre, ppre = 1, 1
        for i in range(2, n + 1):
            tmp = pre
            pre = ppre + pre
            ppre = tmp
        return pre

# Test
t = Solution()
print(t.climbStairs(2))
print(t.climbStairs(3))
print(t.climbStairs(8))


