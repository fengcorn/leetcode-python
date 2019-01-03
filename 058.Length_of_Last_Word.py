class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s.split()   #对字符串进行切片
        if len(s) > 0:
            return len(s[-1])
        return 0

# Test
t = Solution()
print(t.lengthOfLastWord("Hello World"))

