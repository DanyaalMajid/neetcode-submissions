class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for index, num in enumerate(nums):
            if num in seen:
                return True
            else:
                seen[num] = index
        
        return False

