class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r= defaultdict(list)
        for s in strs:
            sorts= ''.join(sorted(s))
            r[sorts].append(s)
        return list(r.values())