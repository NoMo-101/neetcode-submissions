class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, ctn in count.items():
            freq[ctn].append(num)

        for index in range(len(freq) - 1, -1, -1):
            for nums in freq[index]:
                res.append(nums)
                if len(res) == k:
                    return res