class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        while n > 1:
            ans = self.countStr(ans)
            n -= 1
        return ans
    def countStr(self,s):           #输入一个字符串，输出满足报数规则的下一个字符串
        count = 0;ans = "";tmp = s[0]
        for i in range(len(s)):
            if s[i] == tmp:
                count += 1
            else:
                ans += str(count) + tmp
                tmp = s[i]
                count = 1
        ans += str(count) + tmp
        return ans

# Test
t = Solution()
print(t.countAndSay(5))
print(t.countAndSay(6))
print(t.countAndSay(7))
print(t.countAndSay(10))
