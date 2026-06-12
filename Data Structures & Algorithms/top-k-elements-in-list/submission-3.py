class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        '''

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result
