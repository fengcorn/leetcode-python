# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #递归方法
        if not nums:
            return None
        mid = len(nums)//2    #找到中间节点
        root = TreeNode(nums[mid])    #当前节点为根节点
        root.left=self.sortedArrayToBST(nums[:mid]) #小于当前根节点的作为左子树
        root.right=self.sortedArrayToBST(nums[mid+1:])  #大于当前根节点的作为右子树
        return root

# Test
a1 = [-10,-3,0,5,9]
t = Solution()
b1 = t.sortedArrayToBST(a1)
print(b1.val)
print(b1.left.val)
print(b1.right.val)


