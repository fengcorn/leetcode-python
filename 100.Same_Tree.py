# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

# Test
a1 = TreeNode(1)
a1.left = TreeNode(2)
a1.right = TreeNode(3)
a2 = TreeNode(1)
a2.left = TreeNode(2)
a2.right = TreeNode(3)
b1 = TreeNode(1)
b1.left = TreeNode(2)
b2 = TreeNode(1)
b2.right = TreeNode(3)
c1 = TreeNode(1)
c1.left = TreeNode(2)
c1.right = TreeNode(1)
c2 = TreeNode(1)
c2.left = TreeNode(1)
c2.right = TreeNode(2)
t = Solution()
print(t.isSameTree(a1,a2))
print(t.isSameTree(b1,b2))
print(t.isSameTree(c1,c2))

