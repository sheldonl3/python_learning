# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        dic = defaultdict(int)

        def houxu(root):
            if root == None:
                return ''
            left = houxu(root.left)
            right = houxu(root.right)
            tmp = left + ',' + right + ',' + str(root.val)
            if dic[tmp] == 1:
                res.append(root)
            dic[tmp] += 1
            return tmp

        res = []
        houxu(root)
        return res
