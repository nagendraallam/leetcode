class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_S = Counter(s)
        counter_T = Counter(t)

        if len(s) != len(t):
            return False
        
        for i in range(0, len(s)):
            char = s[i]
            if counter_S[char] != counter_T[char]:
                return False

        return True


        