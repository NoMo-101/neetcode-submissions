class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for i in nums:
            current_num = i
            current_length = 1

            while (current_num + 1) in nums:
                current_num = current_num + 1
                current_length += 1
            
            max_length = max(max_length, current_length)

        return max_length