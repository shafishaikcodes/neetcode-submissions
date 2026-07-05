class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""

        for i in range(len(s)):
            if not s[i].isalnum():
                continue

            s1 += s[i].lower()

        i, j = 0, len(s1) - 1

        while i <= j:
            if s1[i] != s1[j]:
                return False

            i += 1
            j -= 1

        return True