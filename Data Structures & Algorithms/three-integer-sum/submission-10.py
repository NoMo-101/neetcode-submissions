class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue
            l = index + 1
            r = len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                if threeSum > 0:
                    r -= 1
                if threeSum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res