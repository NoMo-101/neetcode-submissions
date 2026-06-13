class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, ctn in count.items():
            freq[ctn].append(num)

        res = []

        for index in range(len(freq) - 1, 0, -1):
            for num in freq[index]:
                res.append(num)
                if len(res) == k:
                    return res
