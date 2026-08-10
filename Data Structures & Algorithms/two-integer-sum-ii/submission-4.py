class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        uniq = set(numbers)
        for i, n1 in enumerate(numbers):
            if target - n1 in uniq and numbers[i + 1:].index(target - n1) >= 0:
                j = numbers[i + 1:].index(target - n1) + i + 1
                return [i + 1, j + 1]