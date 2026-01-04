from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = dict()
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target -  nums[i]
            possibleSolution = numMap.get(complement)
            if possibleSolution and numMap[complement] != i:
                return [i, possibleSolution]
        return []
    
    def twoSumSlow(self, nums: List[int], target: int)->List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
        return []




def main():
    sl1 = Solution()
    testCases = (([2,7,11,15], 9),([3,2,4], 6),([3,3], 6))
    for test in testCases:
        print("fast: " + str(sl1.twoSum(test[0], test[1]))) 
        print("slow: " + str(sl1.twoSumSlow(test[0], test[1]))) 
    
main()