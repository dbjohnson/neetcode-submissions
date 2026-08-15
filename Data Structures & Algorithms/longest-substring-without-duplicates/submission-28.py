from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked = set()

        char2pos = defaultdict(list)
        for i, c in enumerate(s):
            char2pos[c].append(i)

        pos2gap = [-(char2pos[c].pop(0) - (char2pos[c] or [len(s)])[0]) for c in s]

        def longest(s, pos2gap):
            if not s:
                return 0

            checked.add(s)

            mx = 0
            i = 0
            while i < len(s):
                gap = pos2gap[i]
                if gap > mx:
                    remaining = gap
                    for j, gap2 in enumerate(pos2gap[i:i + gap]):
                        if gap2 > mx:
                            if s[i + j:i + j + gap2] not in checked:
                                mx = max(
                                    mx, 
                                    longest(
                                        s[i + j:i + j + gap2], 
                                        pos2gap[i + j:i + j + gap2], 
                                    )
                                )

                        remaining = min(gap2, remaining) - 1
                        if remaining == 0:
                            mx = max(mx, j + 1)
                    i += gap
                else:
                    i += 1
            return mx

        return longest(s, pos2gap)