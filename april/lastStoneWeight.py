class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            stones.sort()
            newStones = stones[:len(stones)-2]
            newStones.append(stones[-1] - stones[-2])
            return self.lastStoneWeight(newStones)

    def lastStoneWeight1(self, stones: [int]) -> int:
        while len(stones) > 1:
            a = max(stones)
            stones.remove(a)
            b = max(stones)
            stones.remove(b)
            stones.append(a-b)
        return stones[0]

    def lastStoneWeight2(self, stones: [int]) -> int:
        while len(stones) > 1:
            a = stones.pop(stones.index(max(stones)))
            b = stones.pop(stones.index(max(stones)))
            stones.append(a-b)
        return stones[0]

xs = [8,9,2,4,1,9]
s = Solution()
print(s.lastStoneWeight1(xs))
