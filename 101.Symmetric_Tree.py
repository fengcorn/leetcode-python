# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def solve(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return solve(p.left, q.right) and solve(p.right, q.left)
            return False
        if root == None:
            return True
        else:
            return solve(root.left, root.right)

# Test
a1 = TreeNode(1)
a2 = a1.left = TreeNode(2)
a3 = a1.right = TreeNode(2)
a4 = a2.left = TreeNode(3)
a5 = a2.right = TreeNode(4)
a6 = a3.left = TreeNode(4)
a7 = a3.right = TreeNode(3)
b1 = TreeNode(1)
b2 = b1.left = TreeNode(2)
b3 = b1.right = TreeNode(2)
b5 = b2.right = TreeNode(3)
b7 = b3.right = TreeNode(3)
t = Solution()
print(t.isSymmetric(a1))
print(t.isSymmetric(b1))

