class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sort_s = tuple(sorted(s))
            anagram_map[sort_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result