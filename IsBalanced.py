# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Space Complexity - o(1)
# Time Complexity - o(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left),height(node.right))

        left = height(root.left)
        right = height(root.right)

        diff = left - right

        if abs(diff)>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)