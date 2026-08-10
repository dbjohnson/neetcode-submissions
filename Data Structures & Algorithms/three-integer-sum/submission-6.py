from itertools import combinations
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        counts = Counter(nums)
        twosum = set([
            n1 + n2
            for i, n1 in enumerate(nums)
            for j, n2 in enumerate(nums)
            if i != j
        ])
        for i, n1 in enumerate(nums):
            if -n1 in twosum:
                for n2 in nums[i + 1:]:
                    if -(n1 + n2) in counts:
                        trip = [n1, n2, -(n1 + n2)]
                        if len(set(trip)) < 3:
                            tripcounts = Counter(trip)
                            for k, n in tripcounts.items():
                                if counts[k] < n:
                                    break
                            else:
                                results.add(tuple(sorted(trip)))
                        else:
                            results.add(tuple(sorted(trip)))

        return list(results)
        
        