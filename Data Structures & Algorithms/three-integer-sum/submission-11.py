from itertools import combinations
from collections import Counter, defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        counts = Counter(nums)
        twosum = defaultdict(set)
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j:
                    twosum[-(n1 + n2)].add((n1, n2))

        for n1 in nums:
            for n2, n3 in twosum[n1]:
                trip = [n1, n2, n3]
                tripcounts = Counter(trip)
                for k, n in tripcounts.items():
                    if counts[k] < n:
                        break
                else:
                    results.add(tuple(sorted(trip)))

        return list(results)
        
        