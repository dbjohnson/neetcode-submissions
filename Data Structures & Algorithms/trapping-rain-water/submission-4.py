class Solution:
    def trap(self, height: List[int]) -> int:
        heightmap = defaultdict(list)
        for i, h in enumerate(height):
            for hh in range(1, h + 1):
                heightmap[hh].append(i)

        return sum(
            (idxs[-1] - idxs[0] + 1)
            for idxs in heightmap.values()
        ) - sum(height)

