class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):#递归
        res=[]
        if root==None:
            return res

        def houxu(root,res):
            if root==None:
                return
            if root.left!=None:
                houxu(root.left,res)
            if root.right!=None:
                houxu(root.right,res)
            res.append(root.val)

        houxu(root,res)
        return res

class Solution2:
    def postorderTraversal(self, root: TreeNode):#栈
        res = []
        if root == None:
            return res
        stack=[root]
        while stack:
            tmp=stack.pop(-1)
            res.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return res[::-1]

