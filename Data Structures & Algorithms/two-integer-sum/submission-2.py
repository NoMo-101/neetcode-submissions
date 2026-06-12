class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevCount = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevCount:
                return [prevCount[diff], i]
            prevCount[j] = i       