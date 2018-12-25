class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

# Test
t = Solution()
print(t.searchInsert([1,3,5,6],5))
print(t.searchInsert([1,3,5,6],2))
print(t.searchInsert([1,3,5,6],7))
print(t.searchInsert([1,3,5,6],0))