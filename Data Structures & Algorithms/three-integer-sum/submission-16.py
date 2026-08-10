from itertools import combinations
from collections import Counter, defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        counts = Counter(nums)
        uniq = set(nums)
        twosums = {
            n1 + n2
            for n1 in uniq
            for n2 in uniq
        }
        for n1 in uniq:
            if -n1 in twosums:
                for n2 in uniq:
                    if n2 != n1 or counts[n1] > 1:
                        twosum = n1 + n2
                        if -twosum in uniq:
                            for n3 in nums:
                                if n3 == -twosum:
                                    trip = [n1, n2, n3]
                                    c = Counter(trip)
                                    for k, n in Counter(c).items():
                                        if counts[k] < n:
                                            break
                                    else:
                                        results.add(tuple(sorted(trip)))

        return list(results)
        
        