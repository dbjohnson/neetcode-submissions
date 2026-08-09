class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prod = 1
        zero_idxs = []
        for n in nums:
            if n != 0:
                full_prod *= n
            else:
                zero_idxs.append(n)

        def prod_except(i):
            if len(zero_idxs) > 1:
                return 0
            elif nums[i] == 0:
                return full_prod
            elif zero_idxs:
                return 0
            else:
                return int(full_prod / nums[i])
        
        return [
            prod_except(i) for i in range(len(nums))
        ]