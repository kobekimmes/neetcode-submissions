class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def bt(i, curr, t):
            if t < 0:
                return

            if t == 0:
                res.append(curr[:])
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                bt(j, curr, t - nums[j])
                curr.remove(nums[j])


        bt(0, [], target)

        return res

