class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} # value : index
        for i, j in enumerate(nums):
            diff = target - j
            if diff in preMap:
                return [preMap[diff], i]
            preMap[j] = i