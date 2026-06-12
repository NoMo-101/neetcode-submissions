class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for index in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)
        for num, ctn in count.items():
            freq[ctn].append(num)
        print(freq)

        res = []

        for index in range(len(freq) - 1, 0, -1):
            for num in freq[index]:
                res.append(num)
                if len(res) == k:
                    return res