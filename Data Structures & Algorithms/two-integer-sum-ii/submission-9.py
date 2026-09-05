class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1

        while l < r:
            intSum = nums[l] + nums[r]
            if intSum < target:
                l += 1
            if intSum > target:
                r -= 1
            if intSum == target:
                return [(l + 1), (r + 1)]