# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        if root.left == None:
            return self.hasPathSum(root.right,sum - root.val)
        if root.right == None:
            return self.hasPathSum(root.left,sum - root.val)
        return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)

# Test
a1 = TreeNode(5)
a2 = a1.left = TreeNode(4)
a3 = a1.right = TreeNode(8)
a4 = a2.left = TreeNode(11)
a6 = a3.left = TreeNode(13)
a7 = a3.right = TreeNode(4)
a8 = a4.left = TreeNode(7)
a9 = a4.right = TreeNode(2)
a10 = a7.right = TreeNode(1)
t = Solution()
print(t.hasPathSum(a1,18))