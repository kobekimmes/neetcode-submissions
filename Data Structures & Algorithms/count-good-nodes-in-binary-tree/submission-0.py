# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node, max_till_now):
            if node:
                if node.val >= max_till_now:
                    return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
                else:
                    return dfs(node.left, max_till_now) + dfs(node.right, max_till_now)
            else:
                return 0

        return dfs(root, -101)