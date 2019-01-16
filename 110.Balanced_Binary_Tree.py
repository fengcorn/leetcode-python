# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #按照求树的最大深度去做，只是中间加一个判断，判断左子树的最大深度和右子树的最大深度之差是否大于1
        if root == None:
            return True
        elif abs(self.maxDepth(root.left) - self.maxDepth(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root): 
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
print(t.isBalanced(a1))


