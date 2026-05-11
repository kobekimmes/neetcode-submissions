# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        q = [root]

        while q:
            n = len(q)
            for i in range(n):
                cur = q.pop(0)

                if cur.left:
                    q += [cur.left]
                if cur.right:
                    q += [cur.right]

                if i == n-1:
                    ans.append(cur.val)

        return ans

                





            