class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            count = tuple(sorted(i))
            res[count].append(i)

        return list(res.values())