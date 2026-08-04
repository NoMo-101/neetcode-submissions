class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            maxSum = max(curr, maxSum)
        return maxSum