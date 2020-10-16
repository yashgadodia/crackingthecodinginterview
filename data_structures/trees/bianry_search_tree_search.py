# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#recursively
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        else:
            if val< root.val:
                return self.searchBST(root.left,val) 
            else:
                return self.searchBST(root.right,val)

#using iteration
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         while root is not None and root.val != val:
#             root = root.left if val < root.val else root.right
#         return root