class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sort_strs = tuple(sorted(i))
            res[sort_strs].append(i)
            
        return list(res.values())