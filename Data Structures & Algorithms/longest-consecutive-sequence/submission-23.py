class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        
        def consecutive(n):
            c = 1
            while n + c in uniq:
                c += 1

            return c

        return max(
            consecutive(n) 
            for n in uniq
            # only check starting elements
            if n - 1 not in uniq
        )