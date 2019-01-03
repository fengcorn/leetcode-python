class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num=int(a,2)+int(b,2)   #字符串转整数，按二进制处理
        ans=bin(num)            #返回按二进制表示整数，形式为'0bxx'
        return ans[2:]

# Test
t = Solution()
print(t.addBinary('11','1'))
print(t.addBinary('1010','1011'))


