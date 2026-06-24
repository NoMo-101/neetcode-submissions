class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sort_str = tuple(sorted(i))
            res[sort_str].append(i)

        return list(res.values())