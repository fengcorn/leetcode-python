class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        i = m - 1
        j = n - 1
        while end >= 0:
            if (j < 0 or nums1[i] > nums2[j]) and i >= 0:#如果数组1中的值大于数组2，或者数组2遍历到头了，并且数组1没有到头
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
            end -= 1

# Test
t = Solution()
nums1 = [1,2,3,0,0,0]
t.merge(nums1,3,[2,5,6],3)
print(nums1)

