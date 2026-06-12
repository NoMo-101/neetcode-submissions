class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sort_s = tuple(sorted(s))
            
            if sort_s in res:
                res[sort_s].append(s)
            else:
                res[sort_s] = [s]

        return list(res.values())