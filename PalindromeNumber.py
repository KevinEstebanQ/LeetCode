class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNum = str(x)
        n = len(stringNum)
        for i in range(n-1):
            j=n-i-1
            if stringNum[i] != stringNum[j]:
                return False
        return True
