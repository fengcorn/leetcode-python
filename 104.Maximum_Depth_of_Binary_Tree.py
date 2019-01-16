# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 深度优先搜索
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Test
a1 = TreeNode(3)
a2 = a1.left = TreeNode(9)
a3 = a1.right = TreeNode(20)
a6 = a3.left = TreeNode(15)
a7 = a3.right = TreeNode(7)
t = Solution()
print(t.maxDepth(a1))

