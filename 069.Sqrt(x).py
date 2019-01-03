class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分法
        lo = 0
        hi = x
        while lo <= hi:
            mid = (hi + lo) // 2
            new = mid ** 2
            if new < x:
                lo = mid + 1
            elif new > x:
                hi = mid - 1
            else:
                return mid
        return hi

# Test
t = Solution()
print(t.mySqrt(4))
print(t.mySqrt(8))


