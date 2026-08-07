class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1

        while l < r:
            numSum = nums[l] + nums[r]
            if numSum == target:
                return [l+1, r+1]
            if numSum < target:
                l += 1
            if numSum > target:
                r -= 1