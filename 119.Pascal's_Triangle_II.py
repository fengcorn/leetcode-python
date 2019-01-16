class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1,1]
        i = 1
        while i < rowIndex:
            tmp = [1]
            for j in range(len(ans) - 1):
                tmp.append(ans[j] + ans[j + 1])
            tmp.append(1)
            ans = tmp[:]
            i += 1
        return ans
        
# Test
t = Solution()
print(t.getRow(5))
print(t.getRow(8))