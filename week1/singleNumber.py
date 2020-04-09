from functools import reduce

class Solution:
    def singleNumber(self, nums):
        return reduce(lambda a,b : a ^ b, nums, 0)

xs = []
xs.append([2,2,1])
xs.append([4,1,2,1,2])

s = Solution()
for x in xs: print(s.singleNumber(x))
