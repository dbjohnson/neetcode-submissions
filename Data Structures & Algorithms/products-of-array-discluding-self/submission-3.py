class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prod = 1
        zeros = 0
        for n in nums:
            if n != 0:
                full_prod *= n
            else:
                zeros += 1

        def prod_except(i):
            if zeros > 1:
                return 0
            elif nums[i] == 0:
                return full_prod
            elif zeros:
                return 0
            else:
                return int(full_prod / nums[i])
        
        return [
            prod_except(i) for i in range(len(nums))
        ]