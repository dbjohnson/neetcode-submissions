class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        
        def consecutive(n):
            if n - 1 in uniq:
                # not a starting element
                return 0

            c = 0
            while n in uniq:
                c += 1
                n += 1

            return c

        return max(
            consecutive(n) 
            for n in uniq
        )