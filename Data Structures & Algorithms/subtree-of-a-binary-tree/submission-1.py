# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(n1, n2):

            if n1 == None and n2 == None:
                return True
            if n1 and n2 and n1.val == n2.val:
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)

            return False



        if not subRoot:
            return True
        if not root:
            return False

        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)