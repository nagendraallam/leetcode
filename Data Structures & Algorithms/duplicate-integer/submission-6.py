class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        
        for index,val in enumerate(nums):
            if val in map:
                return True
            
            map[val] = index

        
        return False
        