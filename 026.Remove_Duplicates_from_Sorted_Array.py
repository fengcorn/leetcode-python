class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        head = 0
        for i in range (0, len(nums)):
            if nums[i] != nums[head]:
                head = head + 1
                nums[head] = nums[i]
        print(nums)
        return head + 1

# Test
t = Solution()
print(t.removeDuplicates([1,1,2]))
print(t.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))