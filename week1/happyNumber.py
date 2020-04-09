class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while True:
            history.append(n)
            nPlus1 = self.step(n)
            if nPlus1 == 1:
                return True
            elif nPlus1 in history:
                return False
            n = nPlus1

    def step(self, n):
        res = 0
        for i in range(len(str(n))):
            res += int(n /10**i % 10) **2
        return res


xs = [19,4,25,123]
s = Solution()
for x in xs: print(s.isHappy(x))
