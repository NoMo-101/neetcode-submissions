class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sort_str = tuple(sorted(s))
            res[sort_str].append(s)
        
        return list(res.values())