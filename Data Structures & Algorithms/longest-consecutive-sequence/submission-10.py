class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        counts = dict()

        def consecutive(n):
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

        for n in nums:
            consecutive(n)

        return max(counts.values())