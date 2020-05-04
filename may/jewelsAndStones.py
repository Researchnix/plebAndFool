# jewels and stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        js = set(J)
        j = 0
        for s in S:
            if s in J:
                j += 1
        return j


J = "aAb"
S = "aAAbbbb"

s = Solution()
print(s.numJewelsInStones(J,S))

