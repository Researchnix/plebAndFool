class Solution:
    def moveZeroesLikeAPleb(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for n in nums:
            if n == 0:
                counter += 1

        for i in range(counter):
            nums.remove(0)
            nums.append(0)


    def moveZeroes(self, nums: [int]) -> [int]:
        return list(filter(lambda x : x != 0, nums)) + list(filter(lambda x : x == 0, nums))

xs = []
xs.append([0,1,0,3,12])

s = Solution()
for x in xs:
    print(s.moveZeroes(x))
