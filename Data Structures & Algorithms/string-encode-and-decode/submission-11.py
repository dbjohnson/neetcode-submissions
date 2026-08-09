from string import printable


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '-'

        for count in range(1, 100):
            for s in printable:
                delim = s * count
                for s2 in strs:
                    if delim in s2:
                        break
                else:
                    return f"{delim}|" + delim.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '-':
            return []
        delim, strings = s.split("|", maxsplit=1)
        return strings.split(delim)
