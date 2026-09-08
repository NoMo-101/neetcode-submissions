class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        res = 0
        l = 0
        r = len(h) - 1
        max_l = h[l]
        max_r = h[r]

        while l < r:
            if max_l < max_r:       
                l += 1
                max_l = max(max_l, h[l])
                res += (max_l - h[l])
            else:
                r -= 1
                max_r = max(max_r, h[r])
                res += (max_r - h[r])
        return res