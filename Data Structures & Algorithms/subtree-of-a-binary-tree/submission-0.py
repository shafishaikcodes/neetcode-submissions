# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is subRoot
        def isSameTree(
            p: Optional[TreeNode],
            q: Optional[TreeNode]
        ) -> bool:
            if p is None or q is None:
                return p is q

            return (
                p.val == q.val
                and isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )
        return isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)