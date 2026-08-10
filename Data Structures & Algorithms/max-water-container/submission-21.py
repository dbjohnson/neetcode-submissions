from collections import defaultdict

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heightmap = defaultdict(list)
        
        for i, h in enumerate(heights):
            heightmap[h].append(i)

        leftmost = sorted(
            [(idxs[0], height) for height, idxs in heightmap.items()], 
        )
        rightmost = sorted(
            [(idxs[-1], height) for height, idxs in heightmap.items()], 
            reverse=True
        )

        mxarea = 0
        mxhl = 0
        for l, hl in leftmost:
            if hl <= mxhl:
                continue
            lim = mxarea / hl
            for r, hr in rightmost:
                if (r - l) < lim:
                    break
                else:
                    area = min([hl, hr]) * (r - l)
                    if area > mxarea:
                        mxhl = hl
                        mxarea = area

        return mxarea
