class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        hmap = {}

        for num in nums:
            if hmap.get(num, False):
                return True
            else:
                hmap[num] = True
        
        return False