#Link: https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3532/

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def performOp(self, root: TreeNode, low: int, high: int) -> [int]:
        result = []
        if root:
            result = self.performOp(root.left, low, high)
            if root.val >= low and root.val <= high:
                result.append(root.val)
            result = result + self.performOp(root.right, low, high)
        return result
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return sum(self.performOp(root, low, high))
