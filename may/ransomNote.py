# ransom note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xs = set(ransomNote)
        for x in xs:
            if ransomNote.count(x) > magazine.count(x):
                return False   
        return True

s = Solution()

print(s.canConstruct("a", "b"))

print(s.canConstruct("aa", "ab"))

print(s.canConstruct("aa", "aab"))
