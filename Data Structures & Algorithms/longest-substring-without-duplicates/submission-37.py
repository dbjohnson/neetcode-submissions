from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        checked = set()

        char2pos = defaultdict(list)
        for i, c in enumerate(s):
            char2pos[c].append(i)

        pos2gap = [-(char2pos[c].pop(0) - (char2pos[c] or [len(s)])[0]) for c in s]

        def longest(start, stop):
            mx = 0
            i = start
            while i < stop:
                gap = pos2gap[i]
                if gap > mx:
                    remaining = gap
                    for j, gap2 in enumerate(pos2gap[i : i + gap]):
                        if gap2 > mx:
                            ssstart = i + j
                            ssstop = ssstart + gap2
                            ss = s[ssstart:ssstop]
                            if ss not in checked:
                                checked.add(ss)
                                mx = max(mx, longest(ssstart, ssstop))

                        remaining = min(gap2, remaining) - 1
                        if remaining == 0:
                            mx = max(mx, j + 1)
                            i += j
                            break
                else:
                    i += 1
            return mx

        return longest(0, len(s))

