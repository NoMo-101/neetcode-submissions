class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l = 0
        r = n
        res = 0

        while l <= r:
            m = l + (r-l//2)
            if nums[m] == target:
                return m 
            #left portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m -1
            # right portion                
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1