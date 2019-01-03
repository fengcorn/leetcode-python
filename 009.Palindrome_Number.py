class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num1 = x
        num2 = 0
        while x > 0:
            num2 = num2 * 10 + x % 10   #求个位数字
            x = x // 10                 #抛去个位剩余的数字
        return num1 == num2

# Test
t = Solution()
print(t.isPalindrome(121))
print(t.isPalindrome(-121))
print(t.isPalindrome(10))
