from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for num in nums]
        map = dict()
        ans = []

        for i in range(len(nums)): # nums : freq
            map[nums[i]] = 1 + map.get(nums[i], 0)

        for k,v in map.items():
            bucket[map.get(k)-1].append(k)

        for i in range(len(nums)-1,-1, -1):
            if len(ans) == k:
                return ans
            if len(bucket[i]) > 0:
                ans.append(bucket[i])
            
                
        return ans
    
def main():
    sl1 = Solution()
    sl1.topKFrequent(nums=[1,2],  k=2)
main()
