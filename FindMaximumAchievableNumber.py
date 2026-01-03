class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
    

def main():
    Solution1 = Solution()
    testCases = ([3,2,7],[4,1,6])
    for i in range(len(testCases)):
        x = Solution1.theMaximumAchievableX(testCases[i][0], testCases[i][1])
        if x == testCases[i][2]:
            print("x: "+str(x)+" expected: "+str(testCases[i][2]))
        else:
            print("error at: " + str(testCases[i]))

main()