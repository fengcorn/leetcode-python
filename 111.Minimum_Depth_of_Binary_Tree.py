# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #若左子树为空，则返回右子树的深度，反之返回左子树的深度
        #如果都不为空，则返回左子树和右子树深度的最小值
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return max(leftDepth, rightDepth) + 1
        return min(leftDepth, rightDepth) + 1

# Test
a1 = TreeNode(3)
a2 = a1.left = TreeNode(9)
a3 = a1.right = TreeNode(20)
a6 = a3.left = TreeNode(15)
a7 = a3.right = TreeNode(7)
t = Solution()
print(t.minDepth(a1))