from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for s in strs:
            grams["".join(sorted(s))].append(s)
        return list(grams.values())