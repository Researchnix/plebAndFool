from collections import Counter

# ransom note


class Pleb:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_ctr = Counter(magazine)

        for char in ransomNote:
            if magazine_ctr[char] > 0:
                magazine_ctr[char] -= 1

            else:
                return False

        return True


class Fool:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        xs = set(ransomNote)
        for x in xs:
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True


s = Fool()

print(s.canConstruct("a", "b"))

print(s.canConstruct("aa", "ab"))

print(s.canConstruct("aa", "aab"))
