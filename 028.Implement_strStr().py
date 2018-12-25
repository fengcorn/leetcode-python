class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(0, len(haystack)):
            k = i
            j = 0
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == len(needle):
                return i
        return -1 if needle else 0

# Test
t = Solution()
print(t.strStr("hello","ll"))
print(t.strStr("aaaaa","bba"))