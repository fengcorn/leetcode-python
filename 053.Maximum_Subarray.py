class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])#当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            maxSum = max(maxSum, preSum)
        return maxSum

# Test
t = Solution()
print(t.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

