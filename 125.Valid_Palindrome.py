class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = []
        for i in s:
            if i.isalnum():         #逐个判断是否为字母或数字
                c.append(i.lower()) #转换为小写并添加到c[]中
        for i in range(len(c)//2):
            if c[i] != c[len(c)-1-i]:
                return False
        return True

# Test
t = Solution()
print(t.isPalindrome("A man, a plan, a canal: Panama"))
print(t.isPalindrome("race a car"))