# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #广度优先搜索
        if not root:
            return []   #为空则返回空列表
        queue=[root]    #使用列表实现队列的功能，首先存储root
        res=[]
        while queue:    #当queue不为空时
            nodes=[]    #存节点，每次循环前置空，每次只装一部分
            node_values=[]  #存节点的值
            for node in queue:
                if node.left:
                    nodes.append(node.left) #将左子树装入队列中
                if node.right:
                    nodes.append(node.right)
                node_values+=[node.val] #因为每次循环node_values都会置空，所以最终结果保存在res里，node_values只是一小部分结果
            res=[node_values]+res   #实现从底到顶，node_values放前面，相当于倒序放置
            queue=nodes #将新添加的节点重新赋值给queue
        return res

# Test
a1 = TreeNode(3)
a2 = a1.left = TreeNode(9)
a3 = a1.right = TreeNode(20)
a6 = a3.left = TreeNode(15)
a7 = a3.right = TreeNode(7)
t = Solution()
print(t.levelOrderBottom(a1))

