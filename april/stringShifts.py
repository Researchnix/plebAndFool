class Solution():
    def stringShift(self, s: str, shift: [[int]]) -> str:
        e = 0
        for op in shift:
            if op[0] == 0:
                e = e - op[1] + len(s)
            elif op[0] == 1:
                e = e + op[1]
        e = e % len(s)
        return  s[len(s)-e:] + s[:len(s)-e]



s = Solution()

#  Output: "cab"
v = "abc"
vs = [[0,1],[1,2]]
print(s.stringShift(v, vs))

#  Output: "efgabcd"
w = "abcdefg"
ws = [[1,1],[1,1],[0,2],[1,3]]
print(s.stringShift(w, ws))
