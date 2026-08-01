# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = None

        def f(node):
            nonlocal k, answer

            if node is None:
                return

            # Visit the left subtree first because it contains smaller values.
            f(node.left)

            # Stop further work once the answer has been found.
            if answer is not None:
                return

            # Visit the current node.
            k -= 1

            # When k becomes 0, this is the kth smallest node.
            if k == 0:
                answer = node.val
                return

            # Visit the right subtree.
            f(node.right)

        f(root)
        return answer