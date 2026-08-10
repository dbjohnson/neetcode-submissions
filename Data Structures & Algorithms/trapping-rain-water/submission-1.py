class Solution:
    def trap(self, height: List[int]) -> int:
        heightmap = defaultdict(list)
        
        for i, h in enumerate(height):
            for hh in range(h + 1):
                heightmap[hh].append(i)

        leftmost = {
            h: idxs[0]
            for h, idxs in heightmap.items()
        }
        rightmost = {
            h: idxs[-1]
            for h, idxs in heightmap.items()
        }
        maxheight = max(heightmap)
        trapped = -sum(height)
        for htest in range(1, maxheight + 1):
            trapped += (rightmost[htest] - leftmost[htest] + 1)
        return trapped

