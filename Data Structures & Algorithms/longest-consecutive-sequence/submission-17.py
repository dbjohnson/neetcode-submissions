class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        counts = dict()
        
        def consecutive(n):
            if n - 1 in uniq:
                return 0
            c = 0
            nn = n
            while nn in uniq:
                if nn in counts:
                    c += counts[nn]
                    break
                c += 1
                nn += 1

            counts[n] = c
            return c

        return max(
            consecutive(n) 
            for n in sorted(uniq, reverse=True)
        )