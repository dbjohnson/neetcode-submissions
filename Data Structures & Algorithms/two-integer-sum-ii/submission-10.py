class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        uniq = set(numbers)
        for i, n1 in enumerate(numbers):
            compl = target - n1
            if compl in uniq:
                try:
                    j = numbers[i + 1:].index(compl) + i + 1
                    return [i + 1, j + 1]
                except ValueError:
                    pass