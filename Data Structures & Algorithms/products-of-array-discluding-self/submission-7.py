class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prod = 1
        zeros = 0
        for n in nums:
            if n != 0:
                full_prod *= n
            else:
                zeros += 1

        def prod_except(n):
            if n == 0 and zeros == 1:
                return full_prod
            elif zeros:
                return 0
            else:
                return int(full_prod / n)
        
        return [
            prod_except(n) for n in nums
        ]