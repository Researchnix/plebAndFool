class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        maxLength = 0
        refs = {}
        csum = 0
        refs[csum] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                csum += 1
            elif nums[i] == 0:
                csum -= 1

            if csum in refs:
                maxLength = max(maxLength, i - refs[csum])
            else:
                refs[csum] = i
        return maxLength


xs = [1,0,1,1,0,0]
s = Solution()
print(s.findMaxLength(xs))


