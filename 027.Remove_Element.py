class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head = 0
        for i in range (0,len(nums)):
            if nums[i] != val:
                nums[head] = nums[i]
                head = head + 1
        return head

# Test
t = Solution()
print(t.removeElement([3,2,2,3],3))
print(t.removeElement([0,1,2,2,3,0,4,2],2))