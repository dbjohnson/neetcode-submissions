from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked = set()
        def longest(s):
            if not s or s in checked:
                return 0
            
            checked.add(s)
                
            char2pos = defaultdict(list)
            for i, c in enumerate(s):
                char2pos[c].append(i)
            
            pos2gap = [
                -(char2pos[c].pop(0) - (char2pos[c] or [len(s)])[0])
                for c in s
            ]
            counter = 0
            remaining = len(s)
            mx = 0
            for i, gap in enumerate(pos2gap):
                counter += 1
                if gap > remaining:
                    mx = max(mx, longest(s[i:i+gap]))

                remaining = min(remaining, gap) - 1
                
                if remaining <= 0:
                    if counter > mx:
                        mx = counter
                    counter = 0
                    remaining = len(s)

            return mx
        
        return longest(s)
