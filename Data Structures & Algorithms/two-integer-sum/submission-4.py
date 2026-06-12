class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff in prev:
                return [prev[diff], index]
            prev[number] = index

    