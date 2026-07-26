class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = {}

        for i in nums:
            numSet[i] = numSet.get(i, 0) + 1
        
        for i, j in numSet.items():
            if j > 1:
                return True
        return False