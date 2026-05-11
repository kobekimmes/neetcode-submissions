# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = [root]

        while q:
            temp = []

            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q += [cur.left]
                if cur.right:
                    q += [cur.right]
                    
                temp.append(cur.val)

            ans.append(temp)

        return ans



