from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        return sorted(counts, key=lambda x: counts[x])[-k:]