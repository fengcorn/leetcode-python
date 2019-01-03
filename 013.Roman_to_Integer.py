class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(0, len(s)-1):
            c = s[i]
            c_behind = s[i+1]
            if dic[c] < dic[c_behind]:
                ans = ans - dic[c]
            else:
                ans = ans + dic[c]
        ans = ans + dic[s[-1]]
        return ans

# Test
t = Solution()
print(t.romanToInt('III'))
print(t.romanToInt('IV'))
print(t.romanToInt('IX'))
print(t.romanToInt('LVIII'))
print(t.romanToInt('MCMXCIV'))
