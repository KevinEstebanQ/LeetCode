class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        best = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            seen.add(s[right])
            best = max(best, right-left+1)


        return best


                        
                    

def main():
    sl1 = Solution()
    print(sl1.lengthOfLongestSubstring("anviaj"))
main()