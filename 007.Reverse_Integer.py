class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        z = 0
        x = abs(x)
        while x:
            z = z * 10 + x % 10
            x = x // 10
        return sign * z if z <= 0x7fffffff else 0

# Test
t = Solution()
print(t.reverse(123))
print(t.reverse(-123))
print(t.reverse(120))
print(t.reverse(1534236469))