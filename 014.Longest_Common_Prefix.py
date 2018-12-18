class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) > 0:
            for i,n in enumerate(strs[0]):
                for j in range(1,len(strs)):
                    if i <= (len(strs[j])-1) and n == strs[j][i]:
                        continue
                    else:
                        return result
                result = result + n
            return result
        else:
            return result

# Test
t = Solution()
print(t.longestCommonPrefix(["flower","flow","flight"]))
print(t.longestCommonPrefix(["dog","racecar","car"]))